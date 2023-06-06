from datetime import datetime
import time
import infer
import generator

N_loop = 100
acts_per_loop = 21
N_line = N_loop*acts_per_loop

error_rate = 2
repeat_rate = 2
lose_rate = 1

file_name_generate = "activities_generated.dat"
file_name_results = "test_results.dat"

k0 = 0
k1 = 0
k2 = 2
k3 = 3

signature_0 = ['k', 'o', 'n', 'l', 'm', 'c', 't', 'u', 'c', 'a']
signature_1 = ['k', 'p', 'n', 'l', 'm', 'c', 't', 'u', 'c', 'a', 'q']
signature_2 = ['k', 'o', 'b', 't', 'u', 'd', 'a']
signature_3 = ['k', 'p', 'b', 't', 'u', 'd', 'a', 'q']
signature_4 = ['k', 'o', 'c', 't', 'u', 'd', 'a']
signature_5 = ['k', 'p', 'c', 't', 'u', 'd', 'a', 'q']
signature_6 = ['k', 'o', 'n']
signature_7 = ['k', 'p', 'n', 'q']
signature_8 = ['k', 'o']
signature_9 = ['k', 'p', 'q']
signature_10 = ['a', 'c', 't', 'u', 'k', 'o', 'c']
signature_11 = ['a', 'c', 't', 'u', 'k', 'p', 'c', 'q']
signature_12 = ['a', 'c', 't', 'u', 'k', 'o']
signature_13 = ['a', 'c', 't', 'u', 'k', 'p', 'q']
signature_14 = ['g', 'v']
signature_15 = ['g', 'w']
signature_16 = ['i', 'j']
signature_17 = ['h']
signature_18 = ['r', 'h']
signature_19 = ['h', 's']
signature_20 = ['e', 'y', 'f', 'x']
signature = [signature_0, signature_1, signature_2, signature_3, signature_4, signature_5, signature_6, signature_7, signature_8, signature_9,
             signature_10, signature_11, signature_12, signature_13, signature_14, signature_15, signature_16, signature_17, signature_18, signature_19, signature_20]

def run_evaluate():
    # generate test events and write them to the file "activities_generated.dat"
    print("Events generating starts.")

    f = open(file_name_generate, 'w')
    f.close()
    f = open(file_name_results, 'w')
    f.close()
    # f=open("result_history.dat",'w')
    # f.close()
    rh=open("result_history.dat",'a')

    with open(file_name_generate, 'w') as ag:
        for i in range(N_loop):
            for j in range(acts_per_loop):
                generator.randomEventWriteInFile(
                    ag, signature[j], error_rate, repeat_rate, lose_rate)
    print("Events generating finished.")


    # infer and determine the correctness, write the results to the file "test_results.dat"
    print("Evaluation starts.")
    right=0
    wrong=0
    with open(file_name_generate, '+r') as ag:
        with open(file_name_results, 'w') as ar:
            for i in range(N_line):
                event_str = ag.readline()
                event_list = []
                for s in event_str:
                    if s != '\n':
                        event_list.append(s)

                correct_sig = i % 21
                LU = infer.act_infer(event_list, signature, k3)
                ar.write(str(i)+':')
                wrong+=1
                for item in LU:
                    if item==correct_sig:
                        right+=1
                        wrong-=1
                    ar.write(str(item)+',')
                ar.write('*'+str(correct_sig)+'\n')
                # print("No.",i,"event_list:",event_list,",the result is:",LU,"correct result:",correct_sig)
            ar.write("*************************\n")
            ar.write("right: "+str(right)+"\nwrong: "+str(wrong)+"\ntotal :"+str(right+wrong)+"\nratio: "+str(right/(right+wrong)))
            current_date_and_time = datetime.now()
            rh.write("*************************\n")
            rh.write(str(current_date_and_time)+'\n')
            rh.write("*************************\n")
            rh.write("right: "+str(right)+"\nwrong: "+str(wrong)+"\ntotal :"+str(right+wrong)+"\nratio: "+str(right/(right+wrong)))
            rh.write("\n\n")
            rh.close()

    print("The current date and time is", current_date_and_time)
    print("Evaluation finished.")

if __name__ == '__main__':
    for i in range(1000):
        run_evaluate()
        time.sleep(1)