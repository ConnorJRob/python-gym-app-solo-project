import pdb
from models.adventurer import Adventurer
from models.lesson import Lesson
from models.enrolment import Enrolment

import repositories.adventurer_repository as adventurer_repository
import repositories.lesson_repository as lesson_repository
import repositories.enrolment_repository as enrolment_repository


# adventurer_repository.delete_all()
# lesson_repository.delete_all()

# adventurer_1 = Adventurer("Zimazz", "Greenwind", "Wizard")
# adventurer_repository.save(adventurer_1)

# adventurer_2 = Adventurer("Eldak", "Belzor", "Ranger")
# adventurer_repository.save(adventurer_2)

# adventurer_3 = Adventurer("Grog", "Strongjaw", "Barbarian")
# adventurer_repository.save(adventurer_3)

# lesson_1 = Lesson("Orcish for Beginners", "Wizards", "A beginner's class in speaking Orcish, making sure to avoid getting killed for saying something about someone's mother by accident")
# lesson_repository.save(lesson_1)

# lesson_2 = Lesson("How and when to use Fireball", "Wizards", "Not all the time.")
# lesson_repository.save(lesson_2)

# lesson_3 = Lesson("When is it a mimic?", "Bards", "Assume always.")
# lesson_repository.save(lesson_3)

# enrolment_1 = Enrolment(adventurer_1, lesson_1)
# enrolment_2 = Enrolment(adventurer_2, lesson_2)
# enrolment_3 = Enrolment(adventurer_3, lesson_3)

# enrolment_repository.save(enrolment_1)
# enrolment_repository.save(enrolment_2)
# enrolment_repository.save(enrolment_3)

enrolment_list = enrolment_repository.select_all()

pdb.set_trace()