@bot.command()
import random
async def el_isi_fikirleri(ctx):
    fikirler = [
        "Plastik şişelerden vazo yapabilirsiniz.",
        "Eski plastik kutulardan saksı yapabilirsiniz.",
        "Plastik kaşıklardan süs eşyası yapabilirsiniz.",
        "Plastik kapaklardan mozaik tablo yapabilirsiniz.",
        "fabrikalarinn bacasina fiter koya bilirsiniz",
        "kirli sulari filterden kecirerek kullanila bilir hale getire bilirsiniz",
        "uzaya gonderilen roketlere gunes paneli koyarak elektirikli roket yapa bilirsiniz"
    ]

    yok_olma_tarihleri = [
        "plastik 1000 yilda yok oluyor",
        "cam 4000 yilda yok oluyor",
        "straforlar 5000 yilda yok oluyor"
    ]

    await ctx.send(random.choice(fikirler))
    await ctx.send(random.choice(yok_olma_tarihleri))
