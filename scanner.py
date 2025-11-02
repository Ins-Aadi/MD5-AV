from engine import hash
def scan_file(file_path,signature):
  try:
    hash_value = hash(file_path)
    if not hash_value :
      return f"hash is not found on {file_path}"
    for sign_type,sign_value in signature :
       if sign_type == 'hash' and hash_value == sign_value :
         return f"!! INFECTED FILE {file_path}"
    with open(file_path, 'r', errors = 'ignore') as f:
        content = f.read()
        for sign_type , sign_value in signature:
                if sign_type == "string" and sign_type in content:
                   return f'string matched file is infected !!'
    return f"{file_path} is safe"
  except Exception as exc:
     return f"Error in scanning {file_path}.{exc}"