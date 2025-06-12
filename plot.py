import h5py
import numpy as np
import matplotlib.pyplot as plt

#402964-0-20250528T173900Z
#402964-1-20250528T174050Z
file_name_reco="test1/g4-rec-0.h5"
file_name_true="test1/g4-tru-0.h5"
file_name_reco="g4-rec-0.h5"
file_name_true="g4-tru-0.h5"
key_reco="/100/frame_loose_lf0"
key_true="/0/frame_deposplat0"
data_reco = h5py.File(file_name_reco, "r")
data_true = h5py.File(file_name_true, "r")
f_true = data_true.get(key_true)
f_reco = data_reco.get(key_reco)
#f_reco_2 = data_reco.get(key_reco_2)
#f_dnn = data_reco.get(key_dnn)
frame_t = np.array(f_true)
frame_r = np.array(f_reco)
#frame_r2 = np.array(f_reco_2)
#frame_d = np.array(f_dnn)
print(frame_r.shape)

channles_to_check = [567,450, 317]
tick_ranges = [
    [200, 300],
    [1800, 1900],
    [5800, 5900],
]
ct_zip = list(zip(channles_to_check, tick_ranges))

do_1d_plot = False
# plt.plot(frame_r[ch,:])
# plt.plot(frame_t[ch,:])
# plt.legend(["looseLF","true"])
# plt.show()
if do_1d_plot:
    for ch, tick_range in ct_zip:
        plt.figure(figsize=(10, 6))
        plt.plot(frame_r[ch, tick_range[0]:tick_range[1]], label='looseLF')
        plt.plot(frame_t[ch, tick_range[0]:tick_range[1]], label='depofluxspat')
        plt.title(f'Channel {ch} - Tick Range {tick_range}')
        plt.xlabel('Tick')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid()
        plt.show()
    


do_2d_plot = True
if do_2d_plot:
    # Create a 2D plot
    plt.figure(figsize=(10, 8))
    # plt.title("2D Heatmap Comparison")

    # Plot reco data
    plt.subplot(1, 2, 1)
    plt.imshow(np.transpose(frame_r[0:800,:],(1,0)), aspect='auto', interpolation='none', cmap='viridis')
    # plt.colorbar(label='Amplitude')
    plt.clim(-1000,1000)
    plt.ylim(6000, 0)
    plt.title('looseLF')
    plt.xlabel('channel')
    plt.ylabel('tick')

    # Plot true data
    plt.subplot(1, 2, 2)
    plt.imshow(np.transpose(frame_t[0:800,:],(1,0)), aspect='auto', interpolation='none', cmap='viridis')
    # plt.colorbar(label='Amplitude')
    plt.clim(-1000,1000)
    plt.ylim(6000, 0)
    plt.title('depofluxspat')
    plt.xlabel('channel')
    plt.ylabel('tick')

    plt.tight_layout()
    plt.show()
