import struct


def file_read(path):
    f = open('c:/Users/Mike/PycharmProjects/information-master_25_03_2021_14-37/information-master/Labs/3/1/samples/sample_2', 'rb')
    d = f.read(48)
    c = d[0:36]
    f.close()
    return d, c


def define_obj_file_type(number) -> str:
    if number == 1:
        return "ET_REL"
    elif number == 2:
        return "ET_EXEC"
    elif number == 3:
        return "ET_DYN"
    elif number == 4:
        return "ET_CORE"
    else:
        return "FALSE!! ERROR"


def define_architecture(arch) -> str:
    if arch == 62:
        return "ELFCLASS64"
    else:
        return "ELFCLASS32"


def solve():
    read_text_1, read_text_2 = file_read("vndsi")

    magic_number = "@16x"
    obj_file_type = "H"
    architecture = "H"
    file_version = "I"
    point_virtual_addr = "L"
    program_header_table_offset = "L"
    section_header_table_offset = "L"

    _all = magic_number + obj_file_type + architecture + file_version + point_virtual_addr + program_header_table_offset + section_header_table_offset

    unpack_turple_date = struct.unpack(_all, read_text_2)

    unpack_turple_date_offset = struct.unpack("@40xI4x", read_text_1)

    file_type = define_obj_file_type(unpack_turple_date[0])
    file_machine = define_architecture(unpack_turple_date[1])
    file_entry = hex(unpack_turple_date[3])
    file_program_header_table_offset = unpack_turple_date[5]
    file_section_header_table_offset = unpack_turple_date_offset[0]
    return file_type, file_machine, file_entry, file_program_header_table_offset, file_section_header_table_offset


print(solve())