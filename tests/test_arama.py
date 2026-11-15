import pytest

from ai_lab.arama import en_pahali, fiyat_araligi, sehre_gore, ucretsizler, sehirde_ara
from ai_lab.etkinlik import Event
from ai_lab.veri import events
from ai_lab.hatalar import EtkinlikBulunamadi

# Bütün testlerde kullanacağımız Event listesi
ETKINLIKLER = [Event(**e) for e in events]


# --- ÖRNEK 1: sonucun uzunluğunu kontrol etmek ---
def test_izmirde_3_etkinlik_var():
    sonuc = sehre_gore(ETKINLIKLER, "İzmir")   # 1) fonksiyonu çağır
    assert len(sonuc) == 3                      # 2) beklediğini söyle


# --- ÖRNEK 2: sonucun kendisini kontrol etmek ---
def test_olmayan_sehirde_bos_liste_doner():
    assert sehre_gore(ETKINLIKLER, "Sivas") == []


# --- SIRA SENDE ---
# Her testteki pytest.fail(...) satırını sil, yerine kendi assert'ünü yaz.

def test_iki_ucretsiz_etkinlik_var():
    sonuc = ucretsizler(ETKINLIKLER)
    assert len(sonuc) == 2


def test_fiyat_araligi_sinirlari_dahil():
    # 300-550 aralığında 300 TL'lik "Caz Akşamı" ve 550 TL'lik "Seramik Atölyesi" de gelmeli.
    # İpucu: önce başlıkları bir listeye çek: [e.title for e in sonuc]
    #        sonra: assert "Caz Akşamı" in basliklar
    sonuc = fiyat_araligi(ETKINLIKLER, 300, 550)
    sonuc_basliklar = [event.title for event in sonuc]
    assert "Caz Akşamı"  in sonuc_basliklar
    assert "Seramik Atölyesi" in sonuc_basliklar

def test_en_pahali_rock_festivali():
    # İpucu: en_pahali bir Event döndürüyor, .title ile başlığına bak.
    sonuc = en_pahali(ETKINLIKLER)
    assert sonuc.title == "Rock Festivali"


def test_en_pahali_bos_listede_hata_verir():
    with pytest.raises(ValueError):
        en_pahali([])

def test_sehre_gore_kucuk_harf():
    """Küçük harfle 'izmir' aratıldığında da (Türkçe karakter duyarlılığıyla) sonuç dönmeli."""
    sonuc = sehre_gore(ETKINLIKLER, "izmir")
    assert len(sonuc) == 3

def test_sehirde_ara(): 
    """- sehirde_ara İzmir'de 3 etkinlik döndürüyor   """
    sonuc_izmir = len(sehirde_ara(ETKINLIKLER, "İzmir"))
    assert sonuc_izmir == 3
 

def test_sehirde_ara_hata():
    """- sehirde_ara Sivas'ta EtkinlikBulunamadi fırlatıyor"""
    with pytest.raises(EtkinlikBulunamadi, match="Sivas"):
        sehirde_ara(ETKINLIKLER, "Sivas")
