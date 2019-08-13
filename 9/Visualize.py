import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

class Visualize:
    def main(self, comments_val, keywords_val, analyzed_val, tot_comments_val):
        # suborn style
        sns.set(style="darkgrid", context="paper", font_scale=1)
        
        # Set up the matplotlib figure
        f, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 10), sharex=False)


        # Grafik komentar
        labels = 'Tidak terkategorikan', 'Mendukung', 'Tidak mendukung'
        sizes = comments_val
        colors = ['gold', 'yellowgreen', 'lightskyblue']
        explode = (0, 0.1, 0)
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        ax1.title.set_text("Analisis komentar video Kimi Hime\n" + "'DEAR BAPAK PRESIDEN JOKO WIDODO....'\n")

        # Grafik keywords and bigram
        x2 = ["K.Positive", "K.Negative", "B.Positive", "B.Negative"]
        y2 = keywords_val
        sns.barplot(x=x2, y=y2, palette="Blues_d", ax=ax2, linewidth=0)
        ax2.axhline(0, color="k", clip_on=False)
        ax2.set_ylabel("Keywords / Bigrams\n" + "(match)")
        
        # tampilkan grafik
        plt.text(0.5, -2.5, "Teranalisa " + str(analyzed_val) + " dari "+ str(tot_comments_val) +" komentar")
        plt.show()

# if __name__ == "__main__":
#     Visualize().main([2, 1, 3], [4, 2, 1, 3], 900)