from PyInstaller.utils.hooks import copy_metadata, collect_data_files, collect_submodules

# main package related hook information
hiddenimports = (
    collect_submodules('$app_name')
)

datas = copy_metadata('$app_name')
datas += collect_data_files('$app_name')

