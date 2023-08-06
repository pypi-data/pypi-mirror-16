import nanosite.templates as templates

import os
from zipfile import ZipFile
import json
from urllib.request import urlopen
from urllib.parse import urljoin

DefaultPackageURL = "http://wanganzhou.com/nanosite/packages/"

def set_package_url(url, top):
    if url and url[-1] != "/": url += "/"  # add trailing slash if necessary
    dot_nanosite = None
    with open(os.path.join(top, ".nanosite"), "r") as f:
        dot_nanosite = json.loads(f.read())
        dot_nanosite["package-url"] = url
    if dot_nanosite:
        with open(os.path.join(top, ".nanosite"), "w") as dnf:
            json.dump(dot_nanosite, dnf, indent=2)

# name: package name
# package_url: package repo URL
# returns whether download succeeded
def download_package(name, package_url, dest):
    filename = name + ".zip"
    url = urljoin(package_url, filename)
    print("Downloading package", name, "from", url)
    try:
        with urlopen(url) as response, \
         open(filename, "wb") as out_file:
            out_file.write(response.read())
        return True
    except:
        return False

# f: ZipFile object of package file
# dot_nanosite: contents of .nanosite file (loaded from JSON)
# force: whether to force override
def install_package(name, f, dot_nanosite, top, ctx, force=False):
    with f.open("rules.json", "rU") as rules_file:
        rules = json.loads(rules_file.read().decode("utf-8"))
        files = rules["files"] if "files" in rules else {}
        dependencies = rules["dependencies"] if "dependencies" in rules else []

        # check dependencies
        installed_packages = dot_nanosite["installed-packages"]
        for dependency in dependencies:
            if dependency not in installed_packages:
                print("Installing dependency", dependency)
                import_package(dependency, top, ctx)

        # go through files
        for filename in files:
            rule = files[filename]
            dest = os.path.join(top, templates.fill_template(rule["dest"], ctx))
            with f.open(filename, "r") as src_file:
                with open(dest, rule["action"]) as dest_file:
                    dest_file.write(src_file.read().decode("utf-8"))

        # add to list of installed packages
        if name not in installed_packages:
            installed_packages.append(name)
        dot_nanosite["installed-packages"] = installed_packages
        with open(os.path.join(top, ".nanosite"), "w") as dnf:
            json.dump(dot_nanosite, dnf, indent=2)
    return True, ""
    
# returns (success (bool), status (string))
# force: whether to force override
def import_package(name, top, ctx, force=False):
    name = name.lower()
    
    # setup package info in .nanosite file if first time
    with open(os.path.join(top, ".nanosite"), "r") as f:
        dot_nanosite = json.loads(f.read())
        if "installed-packages" not in dot_nanosite:
            dot_nanosite["installed-packages"] = []
        if "package-url" not in dot_nanosite:
            dot_nanosite["package-url"] = DefaultPackageURL
        installed_packages = dot_nanosite["installed-packages"]
        package_url = dot_nanosite["package-url"]

        # check if package already installed
        if name in installed_packages and not force:
            return False, name + " already installed"

        # check if package file is in site top. If not, download it
        filename = name + ".zip"
        path = os.path.join(top, filename)
        downloaded_package = False
        if not os.path.isfile(path):
            downloaded_package = True
            success = download_package(name, package_url, path)
            if not success: return False, "Could not find package"

        # install package
        with ZipFile(path, "r") as f:
            success, msg = install_package(name, f, dot_nanosite, top, ctx,
                                           force=force)

        # delete package if downloaded
        if downloaded_package:
            os.remove(path)

        return success, msg
