from progressbar import ProgressBar
def percentage_hp(full_hp, now_hp):
    try:
        pbar = ProgressBar(maxval=full_hp)
        pbar.start()
        if now_hp > 0:
            return pbar.update(now_hp)
        if now_hp <= 0:
            pass
    except ValueError:
        pass