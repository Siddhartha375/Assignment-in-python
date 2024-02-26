for i in range(3,21):
    with open(f"Tables/Multiplecation_table_of_{i}.txt",'w')as f:
        for j in range(1,11):
            f.write(f"{i} x {j} ={i*j}\n")
    break
  
  #tables er vitor e multiplecation_table_of{i} name akta folder e
