from pleno import Pleno
from junior import Junior


jose = Junior('José')
jose.search_unanswered_questions()
jose.show_tasks()

luan = Pleno('Luan')
luan.search_unanswered_questions()
luan.search_courses_of_month()

luan.show_tasks()

print(luan)