#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı ışığı yargılama dairesi. Gerçekten çalışır. Adalet şüphelidir."""

from __future__ import annotations

import argparse
import hashlib
import random
import time


SANIK = "buzdolabi isigi"
DAIRE = "Kapı Açılınca Var Olan Şeyler Genel Müdürlüğü"


def esas_no(kapi: str, tanik: str) -> str:
    ham = f"{kapi}|{tanik}|{int(time.time()) // 60}"
    ozet = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:6].upper()
    return f"2026/ISIK-{ozet}"


def hukmet(kapi: str, tanik: str) -> str:
    if kapi == "acik" and tanik != "yok":
        return (
            "SANIK, gözlem altında suçüstü yakalanmıştır. "
            "Işıldamak serbest bırakılır; fakat gereksiz parlaklık için "
            "bir adet 'off' mırıltısıyla uyarılır."
        )
    if kapi == "acik" and tanik == "yok":
        return (
            "Kapı açık, tanık yok. Sanık muhtemelen yanıyor ama "
            "bunu kanıtlayacak kimse salatalık rafında değil. Beraat."
        )
    if kapi == "kapali":
        return (
            "Kapı kapalı. Sanığın varlığı ispat edilememiştir. "
            "Dosya, karanlıkta bekletilmek üzere raflık edilecektir. "
            "Karar: delil yetersizliğinden düşme."
        )
    return "Usul bozuk. Kapı ne açık ne kapalı. Bu bir kapı değil, felsefe."


def durusma(kapi: str, tanik: str) -> None:
    no = esas_no(kapi, tanik)
    print("=" * 62)
    print(DAIRE)
    print("BUZDOLABI ISIGI YARGILAMA DAIRESİ")
    print(f"Esas no: {no}")
    print(f"Sanık  : {SANIK}")
    print(f"Kapı  : {kapi}")
    print(f"Tanık  : {tanik}")
    print("-" * 62)
    print("Sanık susma hakkını kullandı. Ampul bile konuşmadı.")
    bekle = random.uniform(0.4, 1.1)
    print(f"Heyet {bekle:.2f} saniye müzakere etti. Bu, daire için rekor hız.")
    time.sleep(bekle)
    print("-" * 62)
    print("HÜKÜM:")
    print(hukmet(kapi, tanik))
    if tanik.lower() == "kedi":
        print("Tanık beyanı: miyav. Tercüme talebi reddedildi.")
    print("-" * 62)
    print("İstinaf: mutfak tezgahı. Temyiz: komşunun buzdolabı.")
    print("Karar kesin değildir. Işık da değildir.")
    print("=" * 62)


def main() -> None:
    ayristir = argparse.ArgumentParser(
        description="Buzdolabı ışığını yargıla. Adalet opsiyoneldir."
    )
    ayristir.add_argument(
        "--kapi",
        choices=["acik", "kapali"],
        default="kapali",
        help="kapının hukuki durumu",
    )
    ayristir.add_argument(
        "--tanik",
        default="yok",
        help="tanık adı; kediyse beyan miyav sayılır",
    )
    arg = ayristir.parse_args()
    durusma(arg.kapi, arg.tanik)


if __name__ == "__main__":
    main()
