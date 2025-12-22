class FileManager:
    
    def find_file(self, folder, target_name):
        if not isinstance(folder, dict):
            return folder == target_name

        for name, content in folder.items():
            if name == target_name:
                return True
            
            if isinstance(content, dict):
                found = self.find_file(content, target_name)
                if found:
                    return True
        
        return False

fs = {
    "Documents": {
        "Resume.pdf": "content",
        "Work": {
            "Project.py": "content",
            "data.csv": "content"
        }
    },
    "Photos": {
        "vacation.jpg": "content"
    }
}

manager = FileManager() 
print(f"Поиск 'Project.py': {manager.find_file(fs, 'Project.py')}") 
print(f"Поиск 'Music.mp3': {manager.find_file(fs, 'Music.mp3')}") 

# Сложность алгоритма (Big O): O(N), где N — общее количество элементов 
# (файлов и папок) в структуре. В худшем случае нам придется проверить 
# каждый элемент один раз.