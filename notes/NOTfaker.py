from faker import Faker
fake = Faker()

fake.backstory()

# 'Gronk is a sentient tree who was exiled from his forest for being too violent. He is now revenge-bent and will do anything to reclaim his homeland.'
# 'Dianna is a princess who left her castle to find glory on the battlefield. She is merciless and destroys everything efficiently and effectively.'
# 'Urk is a spirit who enjoys tormenting the weak. He is not particularly strong, but he can always hold his ground.'

print(fake.backstory())