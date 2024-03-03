# -*- coding: UTF-8 -*-
import pandas
import numpy

#numpy.linspace(0,1,5)
# numpy.linspace(0,100,5)
#numpy.linspace(0,10,10)
# まず、numpy の linspace 関数を使用して、0 から 10 までの等間隔の値 100 個の配列を作成します。
# これが x 配列 (x 軸の値) になります。
x = numpy.linspace(0, 10, 100)

# 表示して確認してみましょう
x               

# 次に、この x 配列から関数を作成します。
y_linear = x # 線形、y = x
y_neg_linear = -x # 負の傾きを持つ線形、y = -x
y_parabola = -(x-5)**2 + 1 # 放物線または二次関数。** は Python の指数を表すことに注意してください。
y_abs = -abs(x-5) + 1 # abs()関数を使用した絶対値
y_sine = numpy.sin(2*x) # Numpy sin() を使用したサイン関数

y_neg_linear
y_sine

# 次に、これらの配列をそれぞれ列として使用して pandas DataFrame を構築しましょう。
df = pandas.DataFrame()
df['x'] = x
df['linear'] = y_linear
df['neg_linear'] = y_neg_linear
df['parabola'] = y_parabola
df['abs'] = y_abs
df['sine'] = y_sine

# 最初に Astropy からテーブルをインポートします
from astropy.table import Table

tbl = Table.from_pandas(df)

tbl.colnames
tbl['x']

#url = 'https://github.com/sgkane/sonification_tutorial_one/blob/main/prepared_data.csv?raw=true'
#df = pd.read_csv(url,index_col=0)
#tbl = Table.from_pandas(df)

from astronify.series import SoniSeries
# create a sonification (SoniSeries) object for the linear function
soni_linear = SoniSeries(tbl, time_col='x', val_col='linear') # create a SoniSeries object
soni_linear.note_spacing = 0.05 # adjust the note spacing
soni_linear.sonify() # make the sonification
#soni_linear.play() # and play the sonification

soni_neg_linear = SoniSeries(tbl, time_col='x', val_col='neg_linear')
soni_neg_linear.note_spacing = 0.05
soni_neg_linear.sonify()
#soni_neg_linear.play()

soni_parabola = SoniSeries(tbl, time_col='x', val_col='parabola')
soni_parabola.note_spacing = 0.05
soni_parabola.sonify()
#soni_parabola.play()

soni_abs = SoniSeries(tbl, time_col='x', val_col='abs')
soni_abs.note_spacing = 0.05
soni_abs.sonify()
#soni_abs.play()

soni_sine = SoniSeries(tbl, time_col='x', val_col='sine')
soni_sine.note_spacing = 0.05
soni_sine.sonify()
#soni_sine.play()
#soni_parabola.play()

#numpy.random.normal(loc=0, scale=1, size=100)
noise = numpy.random.normal(loc=0, scale=3, size=100)
y_parabola_noise = y_parabola + noise
# これを新しい列としてテーブルに追加します
# これは DatFrame と同じように機能します。
tbl['parabola_noise'] = y_parabola_noise
# そしてソニファイ！
soni_parabola_noise = SoniSeries(tbl, time_col='x', val_col='parabola_noise')
soni_parabola_noise.note_spacing = 0.05
soni_parabola_noise.sonify()
soni_parabola_noise.play()

