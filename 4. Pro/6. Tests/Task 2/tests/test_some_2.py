from ya_disk import YaDisk
from ya_token import YA_TOKEN


def test_create_folder():
    ya_disk = YaDisk(YA_TOKEN)
    res = ya_disk.create_folder('Test folder')
    files_list = ya_disk.get_files_list()

    assert res == 201

    folder_created = False
    for folder in files_list['_embedded']['items']:
        if folder['name'] == 'Test folder':
            folder_created = True
            break
    ya_disk.delete_folder('Test folder')

    assert folder_created is True