import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.animation as  animation

cmap = [
           '#2E91E5',
           '#1CA71C',
           '#DA16FF',
           '#B68100',
           '#EB663B',
           '#00A08B',
           '#FC0080',
           '#6C7C32',
           '#862A16',
           '#620042',
           '#DA60CA',
           '#0D2A63'] * 100

mpl.rcParams['animation.writer'] = 'html'


def line_chart_race(df, filename=None, title="", figsize=(6.5, 3.5), dpi=144, duration=0.5):
    assert "date" in df.columns, "df should with a column date!"
    assert filename is None or filename.endswith(".html"), "filename should like *.html!"

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    ax.set_facecolor("0.9")

    # 调整spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    def plot_frame(date):
        dfdata = df.loc[df["date"] <= date, :]
        dfdata.index = dfdata["date"]
        idx = range(len(dfdata))

        ax.clear()
        cols = [name for name in dfdata.columns if name != "date"]
        for i, col in enumerate(cols):
            ax.plot(idx, dfdata[col], color=cmap[i], lw=4)
            px, py = idx[-1], dfdata[col].iloc[-1]
            ax.scatter(px, py, color=cmap[i], edgecolor="black",
                       s=200, lw=2.5, zorder=4)

            ax.annotate(col + ":\n" + str(py), xy=(px, py), xycoords="data",
                        xytext=(10, 2), fontweight="bold", color=cmap[i], textcoords="offset points")

        # 调整绘图范围
        xlim = (0, len(df))
        ax.set_xlim(xmin=xlim[0] - (xlim[1] - xlim[0]) / 10, xmax=xlim[1] + (xlim[1] - xlim[0]) / 10)
        values = df[[x for x in df.columns if x != "date"]].values
        ylim = (values.min(), values.max())
        ax.set_ylim(ymin=ylim[0] - (ylim[1] - ylim[0]) / 10, ymax=ylim[1] + (ylim[1] - ylim[0]) / 10)

        # 设置xticks
        n = len(df)
        ticks_num = 12
        delta = int(np.ceil(n / ticks_num))
        ticks = list(range(0, n, delta))
        dates = df["date"].tolist()
        ticklabels = [dates[i] for i in ticks]
        ax.set_xticks(ticks)
        ax.set_xticklabels(ticklabels)

        ax.tick_params(bottom=False, left=False, labelsize=8, direction="in", length=2)

        # 添加辅助元素
        s = dfdata["date"].iloc[-1]
        ax.text(0.5, 0.5, s, va="center", ha="center", alpha=0.3, size=50, transform=ax.transAxes)
        ax.grid(axis="x", color="white", lw=1, ls="-")
        ax.set_title(title, color="black", fontsize=12)

    line_animation = animation.FuncAnimation(fig, plot_frame, frames=df["date"], interval=int(duration * 1000))
    if filename is None:
        try:
            from IPython.display import HTML
            return HTML(line_animation.to_jshtml())
        except ImportError:
            pass
    else:
        line_animation.save(filename)
        return filename


dfdata = pd.read_csv('Pop_data.csv')
dfdata = dfdata.rename({"year": "date"}, axis=1)
for col in dfdata.columns:
    if col != "date":
        dfdata.loc[:, col] = np.round(dfdata.loc[:, col] / 1e8, 4)
dfdata.set_index(dfdata["date"])

html_file = "population_race.html"
html = line_chart_race(dfdata, html_file, title="Population Line Race")
