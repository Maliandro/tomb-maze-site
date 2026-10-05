"""
Tomb Maze: Horror Escape - gizlilik / şartlar / destek sitesi üreticisi.
Metinler aşağıda (TR + EN). Çalıştır:  python build.py
Sayfalar data-tr / data-en nitelikleriyle iki dilli; lang.js dil düğmesini yönetir.
"""
import html, os

APP = "Tomb Maze: Horror Escape"
DATE_TR, DATE_EN = "5 Ekim 2026", "October 5, 2026"
MAIL = "mealidengis@gmail.com"


def attr(s):
    return html.escape(s, quote=True)


def p(tr, en, tag="p"):
    return f'    <{tag} data-tr="{attr(tr)}"\n       data-en="{attr(en)}">{tr}</{tag}>\n'


def h3(tr, en):
    return p(tr, en, "h3")


def page(fname, title_tr, title_en, body, back=True):
    out = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_tr} — {APP}</title>
<meta name="description" content="{APP}: {title_en}.">
<link rel="icon" href="icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <img class="icon" src="icon.png" alt="{APP}">
  <h1 data-tr="{attr(title_tr)}" data-en="{attr(title_en)}">{title_tr}</h1>
  <p class="tag">{APP}</p>
  <button id="lang" class="langbtn">English</button>
</header>

<main>
"""
    if back:
        out += '  <a class="back" href="index.html" data-tr="← Ana sayfa" data-en="← Home">← Ana sayfa</a>\n'
    out += body
    out += f"""</main>

<footer><p>© 2026 Maliandro · <a href="mailto:{MAIL}">{MAIL}</a></p></footer>
<script src="lang.js"></script>
</body>
</html>
"""
    with open(fname, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)


def card(inner):
    return '  <section class="card">\n' + inner + "  </section>\n"


updated = p(f"Son güncelleme: {DATE_TR}", f"Last updated: {DATE_EN}").replace("<p ", '<p class="updated" ', 1)

# ---------------------------------------------------------------- Gizlilik
priv = updated
priv += p(
    f"Bu politika, <strong>{APP}</strong> mobil oyununu (&quot;Uygulama&quot;) kullanırken verilerinizin nasıl işlendiğini açıklar. Uygulama Maliandro tarafından geliştirilmiştir.",
    f"This policy explains how your data is handled when you use the <strong>{APP}</strong> mobile game (the &quot;App&quot;), developed by Maliandro.")

priv += h3("Veri sorumlusu", "Data controller")
priv += p(
    f"Uygulamanın veri sorumlusu, uygulamayı Maliandro adıyla yayımlayan bağımsız geliştirici <strong>Mehmet Ali Dengiş</strong>&#39;tir. Kişisel verilerinize ilişkin her türlü talep için: {MAIL}.",
    f"The data controller for the App is the independent developer who publishes it under the name Maliandro, <strong>Mehmet Ali Dengiş</strong>. For any request about your personal data: {MAIL}.")

priv += h3("Topladığımız veriler", "Data we collect")
priv += p(
    "<strong>Uygulama hesap açmanızı, e-posta vermenizi veya giriş yapmanızı istemez.</strong> Oyun tek kişiliktir ve internetsiz oynanabilir. Oyun ilerlemeniz (ulaştığınız seviye, bulduğunuz hazineler ve Güneş Diski parçaları, ölüm sayısı, Sezgi (ipucu) puanınız, satın alımlarınızın kaydı) ve ayarlarınız (dil, ses, parlaklık, bakış hassasiyeti) yalnızca cihazınızda saklanır ve bize gönderilmez. Geliştirici olarak bir sunucumuz yoktur; sizinle ilgili hiçbir veri bize ulaşmaz. Uygulama kamera, mikrofon, konum, kişiler veya fotoğraflara erişim istemez.",
    "<strong>The App never asks you to create an account, give an email address, or sign in.</strong> The game is single-player and can be played offline. Your progress (the level you reached, treasures and Sun Disk pieces found, death count, your Intuition (hint) points, a record of your purchases) and your settings (language, volume, brightness, look sensitivity) are stored only on your device and are never sent to us. We run no server of our own; no data about you reaches us. The App does not request access to your camera, microphone, location, contacts or photos.")

priv += h3("Reklamlar", "Advertising")
priv += p(
    "Uygulama, <strong>Google AdMob</strong> aracılığıyla reklam gösterir: seviye geçişlerinde ve yeniden başlarken tam ekran reklam, isteğe bağlı olarak da ipucu kazanmak veya öldükten sonra devam etmek için ödüllü reklam. AdMob; reklam sunumu, sıklık sınırlaması ve sahtecilik önleme amacıyla cihaz tanımlayıcılarını (ör. reklam kimliği), yaklaşık konum (IP tabanlı) ve uygulama etkileşim bilgilerini işleyebilir. Bu veriler Google tarafından kendi gizlilik politikası kapsamında işlenir.",
    "The App shows ads through <strong>Google AdMob</strong>: full-screen ads between levels and when restarting, and optional rewarded ads to earn a hint or to continue after dying. AdMob may process device identifiers (e.g. advertising ID), approximate location (IP-based) and app interaction data for ad serving, frequency capping and fraud prevention. This processing is governed by Google's own privacy policy.")
priv += """    <ul>
      <li><a href="https://policies.google.com/privacy" target="_blank" rel="noopener" data-tr="Google Gizlilik Politikası" data-en="Google Privacy Policy">Google Gizlilik Politikası</a></li>
      <li><a href="https://adssettings.google.com" target="_blank" rel="noopener" data-tr="Google Reklam Ayarları" data-en="Google Ad Settings">Google Reklam Ayarları</a></li>
    </ul>
"""
priv += p(
    "Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre'deki kullanıcılara, ilk açılışta reklam kişiselleştirme tercihlerini soran bir onay ekranı gösterilir (Google User Messaging Platform). Tercihinizi cihaz ayarlarından dilediğiniz zaman değiştirebilirsiniz.",
    "Users in the European Economic Area, the UK and Switzerland are shown a consent screen on first launch (Google User Messaging Platform) asking about ad personalisation. You can change your choice at any time in your device settings.")
priv += p(
    "Reklam verileri, uygulamaya gömülü Google Mobile Ads yazılımı (SDK) aracılığıyla, elektronik ortamda ve otomatik yolla, reklam gösterildiği sırada doğrudan Google tarafından toplanır; bu verileri biz göremeyiz, bize yalnızca kimliksiz ve toplu raporlar ulaşır. iOS&#39;ta reklam kimliği yalnızca izin verirseniz kullanılır (App Tracking Transparency); izni Ayarlar &gt; Gizlilik ve Güvenlik &gt; İzleme bölümünden geri alabilirsiniz. Android&#39;de reklam kimliğinizi Ayarlar &gt; Google &gt; Reklamlar bölümünden sıfırlayabilir veya silebilirsiniz. &quot;Reklamları Kaldır&quot; satın alımından sonra tam ekran reklamlar gösterilmez.",
    "Advertising data is collected automatically, by electronic means, directly by Google through the Google Mobile Ads software (SDK) built into the App, at the time an ad is shown; we cannot see this data and only receive anonymous, aggregated reports. On iOS the advertising identifier is used only if you allow it (App Tracking Transparency); you can withdraw this in Settings &gt; Privacy &amp; Security &gt; Tracking. On Android you can reset or delete your advertising ID in Settings &gt; Google &gt; Ads. After the &quot;Remove Ads&quot; purchase, full-screen ads are no longer shown.")

priv += h3("Uygulama içi satın alımlar", "In-app purchases")
priv += p(
    "Oyunun 20 seviyesinin tamamı ücretsizdir. Uygulama isteğe bağlı satın alımlar sunar (Reklamları Kaldır, Kaşif Paketi ve Sezgi paketleri). Satın alımlar tamamen Apple App Store veya Google Play tarafından işlenir; kart numaranız, adınız ve fatura bilgileriniz bize ulaşmaz. İade talepleri de bu mağazalar üzerinden yürütülür.",
    "All 20 levels of the game are free. The App offers optional purchases (Remove Ads, Explorer Pack and Intuition packs). Purchases are handled entirely by the Apple App Store or Google Play; your card number, name and billing details never reach us. Refund requests are also handled through these stores.")

priv += h3("Hukuki dayanak", "Legal basis")
priv += p(
    "<strong>Kişiselleştirilmiş reklam:</strong> yalnızca açık rızanız (iOS izleme izni ve reklam onayı formu). <strong>Kişiselleştirilmemiş reklam ve sahtecilik önleme:</strong> uygulamanın ücretsiz sunulabilmesine yönelik meşru menfaat. <strong>Satın alımlar:</strong> sözleşmenin ifası; tamamen Apple veya Google tarafından yürütülür.",
    "<strong>Personalised ads:</strong> your consent only (the iOS tracking prompt and the ad consent form). <strong>Non-personalised ads and fraud prevention:</strong> the legitimate interest of offering the App for free. <strong>Purchases:</strong> performance of a contract; handled entirely by Apple or Google.")

priv += h3("Verilerin yurt dışına aktarılması", "International data transfers")
priv += p(
    "Reklam verileri doğrudan Google&#39;a (Google LLC, ABD), satın alma bilgileri Apple&#39;a (Apple Inc., ABD) veya Google&#39;a iletilir ve bu şirketlerin yurt dışındaki sunucularında işlenir. <strong>Türkiye&#39;deki kullanıcılar (KVKK m. 9):</strong> kişiselleştirilmiş reklam için yapılan aktarım açık rızanıza dayanır. Rıza vermeden önce bilmeniz gereken risk şudur: ABD&#39;de kişisel veriler Türkiye&#39;dekiyle aynı düzeyde korunmayabilir ve yabancı kamu makamlarının bu verilere erişimi mümkün olabilir. Rıza vermezseniz reklamlar kişiselleştirilmez; yalnızca reklamın gösterilmesi için gereken sınırlı teknik veri, Google ve Apple&#39;ın sunduğu veri koruma taahhütleri çerçevesinde işlenir. <strong>Avrupa Ekonomik Alanı&#39;ndaki kullanıcılar (GDPR):</strong> Google ve Apple, AB-ABD Veri Gizliliği Çerçevesi&#39;ne katılmıştır; aktarımlar Avrupa Komisyonu yeterlilik kararına ve standart sözleşme hükümlerine dayanır.",
    "Advertising data is sent directly to Google (Google LLC, USA), and purchase information to Apple (Apple Inc., USA) or Google, and is processed on these companies&#39; servers abroad. <strong>Users in Türkiye (Article 9 of the Turkish Personal Data Protection Law, KVKK):</strong> the transfer made for personalised advertising relies on your explicit consent. Before consenting, you should know the risk: personal data may not be protected in the USA to the same level as in Türkiye, and foreign public authorities may be able to access it. If you do not consent, ads are not personalised; only the limited technical data needed to show an ad is processed, under the data protection commitments Google and Apple provide. <strong>Users in the European Economic Area (GDPR):</strong> Google and Apple participate in the EU-U.S. Data Privacy Framework; transfers rely on the European Commission&#39;s adequacy decision and on standard contractual clauses.")

priv += h3("Haklarınız", "Your rights")
priv += p(
    "KVKK ve GDPR kapsamında erişim, düzeltme, silme, işlemeye itiraz ve veri taşınabilirliği haklarınız vardır. Geliştirici olarak bizde sizinle ilgili bir kayıt bulunmadığından silinecek bir veri yoktur; oyun verileriniz yalnızca cihazınızdadır. Google&#39;ın işlediği reklam verilerine ilişkin taleplerinizi Google&#39;ın gizlilik araçlarıyla iletebilir, rızanızı yukarıda anlatıldığı gibi her an geri alabilirsiniz. Haklarınızın ihlal edildiğini düşünüyorsanız Türkiye&#39;de Kişisel Verileri Koruma Kurumu&#39;na, Avrupa Ekonomik Alanı&#39;nda bulunduğunuz ülkenin veri koruma otoritesine şikâyette bulunabilirsiniz.",
    "Under the KVKK and the GDPR you have the rights of access, rectification, erasure, objection and data portability. Since we hold no record about you, there is nothing for us to delete; your game data is only on your device. You can direct requests about advertising data processed by Google through Google&#39;s privacy tools, and withdraw your consent at any time as described above. If you believe your rights have been infringed, you may lodge a complaint with the Turkish Personal Data Protection Authority or, in the European Economic Area, with the data protection authority of your country.")

priv += h3("Çocukların gizliliği ve içerik", "Children's privacy and content")
priv += p(
    "Uygulama korku temalı bir oyundur; ürkütücü sahneler ve ani korkutmalar içerir (kan veya vahşet içermez). Çocuklara yönelik değildir ve bilerek 13 yaşın altındaki çocuklardan kişisel veri toplamaz.",
    "The App is a horror-themed game with frightening scenes and jump scares (no blood or gore). It is not directed at children and does not knowingly collect personal data from children under 13.")

priv += h3("Verilerinizin silinmesi", "Deleting your data")
priv += p(
    "Oyun verileriniz yalnızca cihazınızdadır. Uygulamayı kaldırdığınızda tamamı silinir. Ayrıca cihaz ayarlarından uygulamanın verilerini temizleyebilirsiniz. Satın aldığınız kalıcı ürünler (Reklamları Kaldır, Kaşif Paketi) mağaza hesabınıza bağlıdır ve oyundaki &quot;Satın alımları geri yükle&quot; ile geri gelir.",
    "Your game data is only on your device. Uninstalling the App deletes all of it. You can also clear the App&#39;s data from your device settings. Permanent purchases (Remove Ads, Explorer Pack) are tied to your store account and come back with &quot;Restore purchases&quot; in the game.")

priv += h3("Değişiklikler", "Changes")
priv += p("Bu politika güncellenebilir. Değişiklikler bu sayfada yayımlanır ve üstteki tarih güncellenir.",
          "This policy may be updated. Changes are published on this page and the date above is updated.")
priv += h3("İletişim", "Contact")
priv += p(f"Sorularınız için: <a href='mailto:{MAIL}'>{MAIL}</a>", f"For questions: <a href='mailto:{MAIL}'>{MAIL}</a>")
page("privacy.html", "Gizlilik Politikası", "Privacy Policy", card(priv))

# ---------------------------------------------------------------- Şartlar
t = updated
t += h3("Lisans", "Licence")
t += p(f"{APP}, kişisel ve ticari olmayan kullanımınız için size kişisel, devredilemez ve münhasır olmayan bir lisansla sunulur. Oyunun kodu, grafikleri, sesleri ve metinleri Maliandro&#39;ya veya lisans verenlerine aittir. Oyundaki bazı ses efektleri üçüncü taraf lisanslarıyla kullanılmıştır (ör. Little Robot Sound Factory, CC-BY 3.0; Kenney, CC0); atıflar oyunun Emeği Geçenler ekranındadır.",
       f"{APP} is provided to you under a personal, non-transferable, non-exclusive licence for your personal, non-commercial use. The game&#39;s code, graphics, sounds and texts belong to Maliandro or its licensors. Some sound effects are used under third-party licences (e.g. Little Robot Sound Factory, CC-BY 3.0; Kenney, CC0); attributions are in the game&#39;s Credits screen.")
t += h3("Satın almalar ve Sezgi puanı", "Purchases and Intuition points")
t += p("Oyunun tüm seviyeleri ücretsizdir. Sezgi (ipucu) puanları oyun içi bir kolaylıktır; gerçek para değeri yoktur, nakde çevrilemez veya devredilemez. Satın almalar Apple veya Google&#39;ın koşullarına tabidir; iadeler bu mağazalar üzerinden yapılır.",
       "All levels of the game are free. Intuition (hint) points are an in-game convenience; they have no real-money value and cannot be cashed out or transferred. Purchases are subject to Apple&#39;s or Google&#39;s terms; refunds are handled through those stores.")
t += h3("Reklamlar", "Advertising")
t += p("Uygulama reklam içerir. &quot;Reklamları Kaldır&quot; satın alımı seviye arası tam ekran reklamları kaldırır; isteğe bağlı ödüllü reklamlar (ipucu, devam) yine seçmeniz hâlinde izlenebilir.",
       "The App contains ads. The &quot;Remove Ads&quot; purchase removes full-screen ads between levels; optional rewarded ads (hints, continue) remain available if you choose to watch them.")
t += h3("Sağlık uyarısı", "Health notice")
t += p("Oyun korku temalıdır; karanlık sahneler, ani sesler ve korkutucu anlar içerir. Işığa duyarlı epilepsi, kalp rahatsızlığı veya yoğun kaygı yaşıyorsanız dikkatli oynayın. Rahatsız hissederseniz ara verin.",
       "The game is horror-themed, with dark scenes, sudden sounds and frightening moments. Play with care if you have photosensitive epilepsy, a heart condition or severe anxiety. Take a break if you feel unwell.")
t += h3("Garanti reddi", "Disclaimer")
t += p("Uygulama &quot;olduğu gibi&quot; sunulur. Kesintisiz veya hatasız çalışacağı garanti edilmez. Yasaların izin verdiği ölçüde, uygulamanın kullanımından doğan dolaylı zararlardan sorumlu değiliz.",
       "The App is provided &quot;as is&quot;. We do not guarantee it will run uninterrupted or error-free. To the extent permitted by law, we are not liable for indirect damages arising from the use of the App.")
t += h3("Değişiklikler", "Changes")
t += p("Bu şartlar güncellenebilir; güncel hâli her zaman bu sayfadadır.", "These terms may be updated; the current version is always on this page.")
t += h3("Geçerli hukuk", "Governing law")
t += p("Bu şartlara Türkiye Cumhuriyeti hukuku uygulanır. Tüketici olarak bulunduğunuz ülkenin zorunlu tüketici koruma kuralları saklıdır.",
       "These terms are governed by the laws of the Republic of Türkiye. Mandatory consumer protection rules of your country of residence remain unaffected.")
t += h3("İletişim", "Contact")
t += p(f"<a href='mailto:{MAIL}'>{MAIL}</a>", f"<a href='mailto:{MAIL}'>{MAIL}</a>")
page("terms.html", "Kullanım Şartları", "Terms of Use", card(t))

# ---------------------------------------------------------------- Destek
s = p(f"Bir sorun mu yaşıyorsunuz? Aşağıdaki sorulara bakın ya da bize yazın: <a href='mailto:{MAIL}'>{MAIL}</a>. Yazarken cihaz modelinizi ve oyunun sürümünü (Ana menünün altında yazar) eklerseniz daha hızlı yardımcı oluruz.",
      f"Having a problem? Check the questions below or write to us: <a href='mailto:{MAIL}'>{MAIL}</a>. Including your device model and the game version (shown at the bottom of the main menu) helps us reply faster.")
faq = [
    ("Nasıl oynanır?", "How do I play?",
     "Sol alttaki sanal çubukla yürüyün, ekranın sağını kaydırarak bakının. Labirentten çıkış kapısını bulun. Bekçilerin sizi görmesine izin vermeyin; koşmak ses çıkarır. Dolaplara ve lahitlere saklanabilir, nefesinizi tutabilirsiniz.",
     "Walk with the virtual stick at the bottom left and swipe the right side of the screen to look around. Find the exit door of the maze. Don't let the Guardians see you; running makes noise. You can hide in lockers and sarcophagi and hold your breath."),
    ("Çok zor / çok karanlık", "It's too hard / too dark",
     "Ayarlar menüsünden parlaklığı artırabilirsiniz. Takıldığınızda İpucu (Sezgi) ile çıkışın yönünü veya haritayı görebilirsiniz; Sezgi puanı hazine bularak ya da reklam izleyerek kazanılır.",
     "You can raise the brightness in Settings. When stuck, use a Hint (Intuition) to see the direction of the exit or the map; Intuition points are earned by finding treasures or watching an ad."),
    ("Satın alımım görünmüyor", "My purchase is missing",
     "Mağaza menüsünde &quot;Satın alımları geri yükle&quot;ye dokunun. Aynı Apple ID / Google hesabıyla giriş yaptığınızdan emin olun.",
     "Tap &quot;Restore purchases&quot; in the Shop menu. Make sure you are signed in with the same Apple ID / Google account."),
    ("İlerlemem kayboldu", "My progress is gone",
     "İlerleme yalnızca cihazda saklanır; uygulama silinirse veya verileri temizlenirse kaybolur. Kalıcı satın alımlar geri yüklenebilir.",
     "Progress is stored only on the device; it is lost if the app is deleted or its data cleared. Permanent purchases can be restored."),
    ("Reklam tercihimi nasıl değiştiririm?", "How do I change my ad preferences?",
     "iOS: Ayarlar &gt; Gizlilik ve Güvenlik &gt; İzleme. Android: Ayarlar &gt; Google &gt; Reklamlar. Reklamları tamamen kaldırmak için oyundaki &quot;Reklamları Kaldır&quot; ürününü kullanabilirsiniz.",
     "iOS: Settings &gt; Privacy &amp; Security &gt; Tracking. Android: Settings &gt; Google &gt; Ads. To remove ads entirely, use the in-game &quot;Remove Ads&quot; product."),
    ("Dili nasıl değiştiririm?", "How do I change the language?",
     "Ayarlar &gt; Dili değiştir. Oyun İngilizce, Türkçe, İspanyolca, Portekizce (Brezilya), Almanca ve Fransızca destekler.",
     "Settings &gt; Change language. The game supports English, Turkish, Spanish, Portuguese (Brazil), German and French."),
]
for qt, qe, at, ae in faq:
    s += h3(qt, qe) + p(at, ae)
page("support.html", "Destek", "Support", card(s))

# ---------------------------------------------------------------- Ana sayfa
idx = p("Çöken bir piramidin altında, Güneş Diski&#39;nin peşindeki bir kaşifsin. 20 labirent, seni duyan ve gören Bekçiler, tuzaklar ve mühürlü kapılar. Fenerin, nefesin ve cesaretin dışında hiçbir şeyin yok.",
        "You are an explorer hunting the Sun Disk beneath a collapsing pyramid. 20 mazes, Guardians that see and hear you, traps and sealed doors. All you have is your flashlight, your breath and your nerve.")
idx += """    <div class="links">
      <a href="privacy.html" data-tr="Gizlilik Politikası" data-en="Privacy Policy">Gizlilik Politikası</a>
      <a href="terms.html" data-tr="Kullanım Şartları" data-en="Terms of Use">Kullanım Şartları</a>
      <a href="support.html" data-tr="Destek" data-en="Support">Destek</a>
    </div>
"""
page("index.html", APP, APP, card(idx), back=False)
print("ok")
