#from django.db import connection

def count_matching_strings(master, slave):
    count = 0
    master_lower = [mstr.lower() for mstr in master]
    slave_lower = [sstr.lower() for sstr in slave]

    for slave_string in slave_lower:
        if slave_string in master_lower:
            count += 1
    return count

# sla = ['specification', 'document', 'contains', 'software', 'requirements', 'formally', 'structured', 'traceability', 'features', 'implemented', 'contains', 'formal', 'specification', 'verified', 'tested', 'requirements', 'obtained', 'various', 'different']
# mas = ['specification', 'document', 'contains', 'software', 'requirements', 'formally', 'structured', 'traceability', 'features', 'implemented', 'contains', 'formal', 'specification', 'verified', 'tested', 'requirements', 'obtained', 'various', 'different' , 'different' , 'requirements'] 

# a = count_matching_strings(mas , sla)
# score = 0
# if a >= 20:
#     score+=5
# else:
#     score+=(a*0.25)

# print(score)

# def reset_auto_increment_1(model):
#     model.objects.all().delete()
#     table_name = model._meta.db_table
#     connection.cursor().execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY;")

# def reset_auto_increment_2(model):
#     model.objects.all().delete()
#     table_name = model._meta.db_table
#     connection.cursor().execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")

# def reset_auto_increment_3(model):
#     model.objects.all().delete()
#     table_name = model._meta.db_table
#     if connection.vendor == 'postgresql':
#         sequence_name = f"{table_name}_id_seq"
#         connection.cursor().execute(f"ALTER SEQUENCE {sequence_name} RESTART WITH 1;")
#     elif connection.vendor == 'mysql':
#         connection.cursor().execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
#     else:
#         # For other database backends, you may need to provide specific syntax
#         raise NotImplementedError("Auto-increment reset not implemented for this database backend.")

# Example usage:


# Example usage:
#master_list = ["apple", "banana", "orange", "grape", "kiwi"]
#slave_list = ["Kiwi", "ORANGE", "mango", "Apple"]

#result = count_matching_strings(master_list, slave_list)
#print("Count of matching strings:", result)
