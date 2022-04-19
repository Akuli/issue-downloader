from typing import Optional
import other_file
import subfolder.file_in_subfolder
                
same_folder_labeled:Optional[str]
same_folder_labeled=other_file.labeled_return()
same_folder_labeled.capitalize()

same_folder_unlabeled:Optional[str]
same_folder_unlabeled=other_file.unlabeled_return()
same_folder_unlabeled.capitalize()

sub_folder_labeled:Optional[str]
sub_folder_labeled=subfolder.file_in_subfolder.labeled_return()
sub_folder_labeled.capitalize()

sub_folder_unlabeled:Optional[str]
sub_folder_unlabeled=subfolder.file_in_subfolder.unlabeled_return()
sub_folder_unlabeled.capitalize()
