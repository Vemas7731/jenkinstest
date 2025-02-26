import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#DATA WRANGLING

#dataset
df_Aotizhongxin = pd.read_csv('PRSA_Data_Aotizhongxin_20130301-20170228.csv')
df_Changping = pd.read_csv('PRSA_Data_Changping_20130301-20170228.csv')
df_Dingling = pd.read_csv('PRSA_Data_Dingling_20130301-20170228.csv')
df_Dongsi = pd.read_csv('PRSA_Data_Dongsi_20130301-20170228.csv')
df_Guanyuan = pd.read_csv('PRSA_Data_Guanyuan_20130301-20170228.csv')
df_Gucheng = pd.read_csv('PRSA_Data_Gucheng_20130301-20170228.csv')
df_Huairou = pd.read_csv('PRSA_Data_Huairou_20130301-20170228.csv')
df_Nongzhanguan = pd.read_csv('PRSA_Data_Nongzhanguan_20130301-20170228.csv')
df_Shunyi = pd.read_csv('PRSA_Data_Shunyi_20130301-20170228.csv')
df_Tiantan = pd.read_csv('PRSA_Data_Tiantan_20130301-20170228.csv')
df_Wanliu = pd.read_csv('PRSA_Data_Wanliu_20130301-20170228.csv')
df_Wanshouxigong = pd.read_csv('PRSA_Data_Wanshouxigong_20130301-20170228.csv')

#ambil fitur yang dibutuhkan
df_Wanliu = df_Wanliu[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Aotizhongxin = df_Aotizhongxin[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Changping = df_Changping[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Dingling = df_Dingling[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Dongsi = df_Dongsi[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Guanyuan = df_Guanyuan[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Gucheng = df_Gucheng[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Huairou = df_Huairou[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Nongzhanguan = df_Nongzhanguan[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Shunyi = df_Shunyi[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Tiantan = df_Tiantan[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]
df_Wanshouxigong = df_Wanshouxigong[['year', 'month', 'day', 'PM2.5', 'station', 'WSPM', 'RAIN','SO2','NO2','CO','O3']]

#gabungin dataset
df_allstation = pd.concat([df_Wanliu, df_Aotizhongxin, df_Changping,
                            df_Dingling, df_Dongsi, df_Guanyuan,
                            df_Gucheng, df_Huairou, df_Nongzhanguan,
                            df_Shunyi, df_Tiantan, df_Wanshouxigong])
print('DataFrame Awal : ', df_allstation)

#satuin tiga fitur ('year', 'month', 'day') jadi satu fitur aja ('date')
df_allstation['date'] = pd.to_datetime(df_allstation[['year', 'month', 'day']])
df_allstation.drop(columns=['year', 'day'], inplace=True)
print(df_allstation)

#cek missing values
cek_missing = df_allstation.isnull().sum()
print(cek_missing)

#interpolation missing values karena dataset bertipe time series
df_allstation['PM2.5'].interpolate(method='linear', limit_direction='forward', inplace=True)
df_allstation['WSPM'].interpolate(method='linear', limit_direction='forward', inplace=True)
df_allstation['RAIN'].interpolate(method='linear', limit_direction='forward', inplace=True)
df_allstation['SO2'].interpolate(method='linear', limit_direction='forward', inplace=True)
df_allstation['NO2'].interpolate(method='linear', limit_direction='forward', inplace=True)
df_allstation['CO'].interpolate(method='linear', limit_direction='forward', inplace=True)
df_allstation['O3'].interpolate(method='linear', limit_direction='forward', inplace=True)

#cek missing values
cek_missing = df_allstation.isnull().sum()
print(cek_missing)

#cek duplikat
cek_duplikat = df_allstation.duplicated().sum()
print('Duplikat : ', cek_duplikat)

#hapus duplikat
df_allstation.drop_duplicates(inplace=True)
cek_duplikat = df_allstation.duplicated().sum()
print(df_allstation)

print('Duplikat : ', cek_duplikat)

#cek outlier
jarak_interkuartil = np.percentile(df_allstation['PM2.5'], 75) - np.percentile(df_allstation['PM2.5'], 25)

q1, q3 = np.percentile(df_allstation['PM2.5'], 25), np.percentile(df_allstation['PM2.5'], 75)
cut_off = jarak_interkuartil * 1.5
minimum, maximum = q1 - cut_off, q3 + cut_off

[x for x in df_allstation['PM2.5'] if x < minimum or x > maximum][0]

q1, q3 = np.percentile(df_allstation['PM2.5'], 25), np.percentile(df_allstation['PM2.5'], 75)

#hilangin outlier PM 2.5
sebelumoutlier = df_allstation.shape[0]
q1 = (df_allstation['PM2.5'].quantile(0.25))
q3 = (df_allstation['PM2.5'].quantile(0.75))
iqr = q3-q1

maximum = q3 + (1.5*iqr)
minimum = q1 - (1.5*iqr)

kondisi_lower_than = df_allstation['PM2.5'] < minimum
kondisi_more_than = df_allstation['PM2.5'] > maximum

df_allstation.drop(df_allstation[kondisi_lower_than | kondisi_more_than].index, inplace=True)
setelahoutlier = df_allstation.shape[0]
outliertereliminasi = sebelumoutlier - setelahoutlier

print('Jumlah Outlier yang Dibuang : ', outliertereliminasi)

#hilangin outlier WSPM 
sebelumoutlier = df_allstation.shape[0]
q1 = (df_allstation['WSPM'].quantile(0.25))
q3 = (df_allstation['WSPM'].quantile(0.75))
iqr = q3-q1

maximum = q3 + (1.5*iqr)
minimum = q1 - (1.5*iqr)

kondisi_lower_than = df_allstation['WSPM'] < minimum
kondisi_more_than = df_allstation['WSPM'] > maximum

df_allstation.drop(df_allstation[kondisi_lower_than | kondisi_more_than].index, inplace=True)
setelahoutlier = df_allstation.shape[0]
outliertereliminasi = sebelumoutlier - setelahoutlier

print('Jumlah Outlier yang Dibuang : ', outliertereliminasi)

#Outlier RAIN
sebelumoutlier = df_allstation.shape[0]
q1 = df_allstation['WSPM'].quantile(0.25)
q3 = df_allstation['WSPM'].quantile(0.75)
iqr = q3 - q1

maximum = q3 + (1.5 * iqr)
minimum = q1 - (1.5 * iqr)

kondisi_lower_than = df_allstation['WSPM'] < minimum
kondisi_more_than = df_allstation['WSPM'] > maximum

df_allstation.drop(df_allstation[kondisi_lower_than | kondisi_more_than].index, inplace=True)
setelahoutlier = df_allstation.shape[0]
outliertereliminasi = sebelumoutlier - setelahoutlier

print('Jumlah Outlier yang Dibuang :', outliertereliminasi)

#cek jumlah baris
rows = df_allstation.shape[0]
print('Jumlah sampel : ', rows)


#EDA

print(df_allstation['PM2.5'].describe())

#korelasi kecepatan angin dan tingkat PM 2.5
korelasiangin = df_allstation[['WSPM', 'PM2.5']].corr()
print('Korelasi kecepatan angin dengan tingkat polusi : ')
print(korelasiangin)

#korelasi hujan dan tingkat PM 2.5
korelasiangin = df_allstation[['RAIN', 'PM2.5']].corr()
print('Korelasi hujan dengan tingkat polusi : ')
print(korelasiangin)


#DATA VISUALIZATION
#korelasi angin dan hujan heatmap
correlation_matrix = df_allstation[['WSPM', 'RAIN', 'PM2.5']].corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True, linewidths=0.5, cbar_kws={"shrink": .8})
plt.title('Heatmap Korelasi Kecepatan Angin, Hujan, dan PM2.5', fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

#line chart kecepatan angin tahunan
df_angindanhujantahunan = df_allstation.groupby('date')[['WSPM', 'RAIN']].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='WSPM', data=df_angindanhujantahunan, marker='o', color='blue', label='WSPM')
plt.title('Rata-rata Kecepatan Angin Tahunan', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Kecepatan Angin (WSPM)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#line chart curah hujan tahunan
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='RAIN', data=df_angindanhujantahunan, marker='o', color='green', label='RAIN')
plt.title('Rata-rata Curah Hujan Tahunan', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Curah Hujan (RAIN)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#kapan biasanya lonjakan polusi udara
df_lonjakanpolusi = df_allstation.groupby('date')[['PM2.5']].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='PM2.5', data=df_lonjakanpolusi, marker='o', color='blue', label='WSPM')
plt.title('Persebaran Polusi Udara Per Tahun', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Konsentrasi PM2.5', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#rata rata pm 2.5 per bulan
df_rata2_pm_per_bulan = df_allstation.groupby('month')['PM2.5'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='PM2.5', data=df_rata2_pm_per_bulan, color='blue')
plt.title('Rata-rata Konsentrasi PM2.5 per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Rata-Rata Konsentrasi PM2.5', fontsize=12)
plt.tight_layout()
plt.show()

#rata rata gas SO2 NO2 CO O3 per bulan
#SO2
df_so2_per_bulan = df_allstation.groupby('month')['SO2'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='SO2', data=df_so2_per_bulan, color='blue')
plt.title('Rata-rata Konsentrasi SO2 per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Rata-Rata Konsentrasi SO2', fontsize=12)
plt.tight_layout()
plt.show()

#NO2
df_no2_per_bulan = df_allstation.groupby('month')['NO2'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='NO2', data=df_no2_per_bulan, color='blue')
plt.title('Rata-rata Konsentrasi NO2 per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Rata-Rata Konsentrasi NO2', fontsize=12)
plt.tight_layout()
plt.show()

#CO
df_co_per_bulan = df_allstation.groupby('month')['CO'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='CO', data=df_co_per_bulan, color='blue')
plt.title('Rata-rata Konsentrasi CO per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Rata-Rata Konsentrasi CO', fontsize=12)
plt.tight_layout()
plt.show()

#O3
df_o3_per_bulan = df_allstation.groupby('month')['O3'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='O3', data=df_o3_per_bulan, color='blue')
plt.title('Rata-rata Konsentrasi O3 per Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Rata-Rata Konsentrasi O3', fontsize=12)
plt.tight_layout()
plt.show()

#korelasi gas SO2 NO2 CO O3 dengan tingkat pm2.5
#SO2
korelasiso2 = df_allstation[['SO2', 'PM2.5']].corr()
print('Korelasi Munculnya Gas SO2 dengan Waktu Polusi : ')
print(korelasiso2)

#NO2
korelasino2 = df_allstation[['NO2', 'PM2.5']].corr()
print('Korelasi Munculnya Gas NO2 dengan Waktu Polusi : ')
print(korelasino2)

#CO
korelasico = df_allstation[['CO', 'PM2.5']].corr()
print('Korelasi Munculnya Gas CO dengan Waktu Polusi : ')
print(korelasico)

#O3
korelasio3 = df_allstation[['O3', 'PM2.5']].corr()
print('Korelasi Munculnya Gas O3 dengan Waktu Polusi : ')
print(korelasio3)

# Mengambil fitur yang relevan untuk korelasi
df_korelasi_gas = df_allstation[['PM2.5', 'SO2', 'NO2', 'CO', 'O3']]

# Menghitung korelasi
korelasi_gas = df_korelasi_gas.corr()

# Visualisasi heatmap korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(korelasi_gas, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Korelasi PM2.5 dengan Gas (SO2, NO2, CO, O3)', fontsize=14)
plt.tight_layout()
plt.show()


