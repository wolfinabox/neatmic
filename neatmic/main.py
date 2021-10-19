from neatmic.mainapp import main

if __name__ == "__main__":
    main()


# from queue import Empty
# import soundcard as sc
# import numpy as np
# from multiprocessing import Queue
# speakers=sc.all_speakers()
# mics=sc.all_microphones()
# # print('Speakers:')
# # for speaker in speakers:
# #     print('\t'+speaker.name)

# # print('Mics:')
# # for mic in mics:
# #     print('\t'+mic.name)
# for mic in mics:
#     print(mic.name)
# speaker=speakers[0]
# microphone=mics[0]


# offset_ms=0
# samplerate=48000
# data_queue=Queue()
# max_vol=0
# with microphone.recorder(samplerate=samplerate,blocksize=None) as mic,\
#         speaker.player(samplerate=samplerate,blocksize=None,channels=2) as spkr:

#     print(f'Playing "{microphone.name}" to "{speaker.name}"')
#     print(f'Speaker Buffersize: {spkr.buffersize}, Mic Buffersize:{mic.buffersize}')

#     while True:
#         #record mic
#         data1:np.ndarray=mic.record(numframes=480)
#         data1=data1
#         #calculate length of the sample
#         sample_length_ms=(data1.shape[0]/samplerate)*1000
#         #how many samples until audio
#         delay_samples=(offset_ms//sample_length_ms)
       
#         data_queue.put_nowait(data1)
#         if data_queue.qsize()>=delay_samples:
#             try:
#                 data=data_queue.get_nowait()
#                 volume=(np.linalg.norm(data)*10)%100
#                 # spkr.play(data)
#                 if volume>max_vol:max_vol=volume
#                 print(f'{int(volume)}, max={int(max_vol)}')
#             except Empty:
#                 continue


 # print(sample_size)
        # data2:np.ndarray=mic2.record(numframes=480)

        #this puts one mic on one channel, one on the other
        #final_data=np.column_stack((data1,data2))

        #this averages values from both mics, kinda?
        #final_data=np.mean(np.array([data1,data2]),axis=0)
        
        #adds both mics together, similar to above but louder
        # final_data=data1+data2

        # print(data1.shape,data2.shape,final_data.shape)
        # sp.play(data1)