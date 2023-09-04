valor_sem_taxa = 100
taxa_icms = 18

valor_icms = (valor_sem_taxa * taxa_icms) / 100
valor_com_taxa =  valor_sem_taxa + valor_icms

print(f"Preço do produto com icms é: R$ {valor_com_taxa}")