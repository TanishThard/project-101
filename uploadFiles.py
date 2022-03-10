
import os
import dropbox
from dropbox.files import WriteMode



class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        #enumerate local files recurssively
        for root,dirs,file in os.walk(file_from):
            for filename in file:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)

                with open(local_path, 'rb')as f:
                     dbx.files_upload(f.read(), dropbox_path ,mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.BDJjvrLbW6WZVFV_49_g0FVlZ5sZJLrEBDWeRv4JO7IHZRJt9bvjFyI5OTs346XTR3g-BifCErowVgBNJbsb-YNK4Htjv8H_H4wBLIA79gtKbsPlhB_wafhmNwf3tb6FwWWzzKxTfEmx'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer:")
    file_to = input("enter the full path to upload to drop box:")
    transferData.upload_file(file_from, file_to)
    print("the file has been moved.")


main()
