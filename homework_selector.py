import glob, os

class file_reader():
    def __init__(self, folder_name : str):
        os.chdir(folder_name)
        self.folder_name    = folder_name 
        self.hard_questions = []
        self.easy_questions = []
        self.files          = [file for file in glob.glob("*.icl")]
        self.read_files_into_arrays()
    def read_files_into_arrays(self):
        for file in self.files:
            opened_file   = open(file)
            file_string   = opened_file.read()
            two_questions = file_string.split("_end_1")
            self.easy_questions.append(two_questions[0])
            self.hard_questions.append(two_questions[1].split("_end_2")[0])
            opened_file.close()

    def create_new_files(self,day = 1):
        os.chdir("..")
        new_dir = "Homework_" + str(day)
        os.mkdir(new_dir)
        os.chdir(new_dir)

        created_files = 1
        for questions in self.easy_questions:
            for question in self.hard_questions:
                file_name   = "homeWork_" + str(day) + "_v_" + str(created_files) 
                opened_file = open(file_name + ".icl" , "w")
                header_string  = "module " + file_name + "\n" + "import StdEnv" + "\n\n\n"
                opened_file.write(header_string)
                opened_file.write(questions + "\n\n\n")
                opened_file.write(question)

                created_files += 1

abc = file_reader("./files")
abc.create_new_files(1)