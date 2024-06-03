def create_test_file():
    file_path = '/var/jenkins_home/Test.txt'
    with open(file_path, 'w') as file:
        file.write("Este es un test de funcionamiento")

if __name__ == "__main__":
    create_test_file()
