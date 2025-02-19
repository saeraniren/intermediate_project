import os 
import pandas as pd
from pathlib import Path
from multiprocessing import Pool

# 데이터 파일이 저장된 디렉토리 설정
DATA_DIR = Path("./data")

class BaseLoader:
    def __init__(self, class_name):
        self.class_name = class_name
    
    def load_file(self, file_path):
        # 주어진 파일을 로드하는 함수
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def load_files(self):
        # 해당 클래스와 관련된 파일을 필터링하고 로드
        class_files = [f for f in DATA_DIR.iterdir() if self.class_name in f.name and f.is_file()]

        with Pool(processes=os.cpu_count()) as pool:
            dataframes = pool.map(self.load_file, class_files)

            return [df for df in dataframes if df is not None]

class click(BaseLoader):
    def __init__(self):
        super().__init__("click")

    @staticmethod
    def cancel_plan_button():
        file_name = "click.cancel_plan_button.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
    
    @staticmethod
    def content_page_more_review_button():
        file_name = "click.content_page_more_review_button.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

    @staticmethod    
    def content_page_start_content_button():
        file_name = "click.content_page_start_content_button.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

    @staticmethod    
    def lesson_page_related_comment_box():
        file_name = "click.lesson_page_related_question_box.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

class complete(BaseLoader):
    def __init__(self):
        super().__init__("complete")

    @staticmethod
    def lesson():
        file_name = "complete.lesson.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
    @staticmethod
    def signup():
        file_name = "complete.signup.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
    @staticmethod
    def subscription():
        file_name = "complete.subscription.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

class end(BaseLoader):
    def __init__(self):
        super().__init__("end")

    @staticmethod
    def content():
        file_name = "end.content.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

class enter(BaseLoader):
    def __init__(self):
        super().__init__("enter")

    @staticmethod
    def content_page():
        file_name = "enter.content_page.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

    @staticmethod
    def lesson_page():
        file_name = "enter.lesson_page.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
    @staticmethod
    def main_page():
        file_name = "enter.main_page.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
    @staticmethod
    def payment_page():
        file_name = "enter.payment_page.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
    @staticmethod
    def signup_page():
        file_name = "enter.signup_page.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

class renew(BaseLoader):
    def __init__(self):
        super().__init__("renew")

    @staticmethod
    def subscription():
        file_name = "renew.subscription.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
class resubscribe(BaseLoader):
    def __init__(self):
        super().__init__("resubscribe")

    @staticmethod
    def subscription():
        file_name = "resubscribe.subscription.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")

class start(BaseLoader):
    def __init__(self):
        super().__init__("start")

    @staticmethod
    def content():
        file_name = "start.content.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
    @staticmethod
    def free_trial():
        file_name = "start.free_trial.csv"
        file_path = DATA_DIR / file_name
        if file_path.exists():
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{file_path} not found")
        
__all__ = ['click', 'complete', 'end', 'enter', 'renew', 'resubscribe', 'start']