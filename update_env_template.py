
def update_env_template():
  """Updates .env-template file from the .env file, stripping out passwords but keeping keys"""
  env_file = open(".env", "r")
  env_lines = env_file.readlines()
  env_file.close()

  env_template_file = open(".env-template", "w")
  env_template_file.writelines([ line.split("=")[0] + "=\n" for line in env_lines ])
  env_template_file.close()

if __name__ == "__main__":
  update_env_template()
