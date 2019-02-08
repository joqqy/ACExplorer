from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '71FDA747'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(4, out_file)
		file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.read_str(33, out_file, indent_count)