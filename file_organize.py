from pathlib import Path
from shutil import copy
# 
# Naming using the format 

# scan info - patient ID - scan ID - slice number

large_out = Path("large_cells_out")
no_large_out = Path("no_large_cells_out")

large_out.mkdir(parents=True, exist_ok=True)
no_large_out.mkdir(parents=True, exist_ok=True)

lidc_path = "selected-subset"

large_cell = "large_cells"

no_large_cell = "no_large_cells"

lidc_dir1 = Path(__file__).parent.resolve() / lidc_path / large_cell
lidc_dir2 = Path(__file__).parent.resolve() / lidc_path / no_large_cell

curr_path = None
correct_naming = None

def copy_and_rename(lidc_dir, out_parent_dir):
    for child in list(lidc_dir.rglob('*/*')):

        slices = [x for x in list(child.rglob("*.dcm")) if x.is_file()]
        
        for curr_path in sorted(slices):

            scan_num = curr_path.parents[2].name.split("-")[-1]
            patient_id = curr_path.parents[1].name.split("-")[-1]
            scan_id = curr_path.parent.name.split("-")[-1]
            slice_id = curr_path.stem[2:]

            correct_naming = scan_num + "-" + patient_id + "-" + scan_id + "-" + slice_id + ".dcm"



            dest = out_parent_dir / correct_naming

            print(dest)
            copy(curr_path, dest)

# renaming and copy all large cell to large_cell_out
copy_and_rename(lidc_dir1, large_out)

# renaming and copy all no large cell to no_large_cell_out
copy_and_rename(lidc_dir2, no_large_out) 
