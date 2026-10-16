# Project tasks

## M0 — CLI doğrulaması

- Teknik durum: `verified` — aşağıdaki normal kurulum koşulları için.
- Uygulayan: Kullanıcı ve Codex eşli çalışma; doğrulama komutlarını kullanıcı çalıştırdı. Bu görev kaydını kullanıcının isteğiyle Codex hazırladı.
- Öğrenilecek kavram: Komutun çıkış kodu (exit code) ile test başarısının farkı; standart çıktı (stdout) ve hata çıktısı (stderr) kontrolleri.

### Teknik çıktı

`tests/integration/test_cli.py` iki davranışı kontrol eder:

1. `--help`: çıkış kodu `0` ve stdout içinde `--help`.
2. `--unknown`: çıkış kodu `2` ve stderr içinde hem `unrecognized arguments` hem de `--unknown`.

Testler kurulu CLI giriş noktasını ayrı süreçte, geçici çalışma dizininden ve Python'ın `-I` seçeneğiyle çalıştırır. `check=False`, çıkış kodunun testteki `assert` ifadeleriyle değerlendirilmesini sağlar.

### Doğrulama kanıtı

Kullanıcının paylaştığı terminal çıktısında Python 3.12.15 ile yeni geçici sanal ortama `uv sync --locked --no-editable` kurulumu yapıldı. Bu ortamın Python'ıyla `-I -m pytest -q tests/integration/test_cli.py` çalıştırıldı: **2 passed in 0.06s**. Bu çalıştırmada `chflags` uygulanmadı.

Kontrol aynı makine ve mevcut uv önbelleğiyle yapıldı. Bu kayıt hazırlanırken testler yeniden çalıştırılmadı. Sonuç yalnızca sınanan iki CLI davranışını doğrular; M0'ın veya tespit sisteminin tamamlandığı anlamına gelmez.

### Birlikte değerlendirilen öğrenme

Kullanıcı lint ile davranış testini ayırdı. Bilinmeyen seçenek için `0` dönmesinin komut açısından başarı bildirse de `2` bekleyen testi başarısız kılacağı birlikte açıklandı. Ardından kullanıcı, stderr içinde `--unknown` bulunmadığında ilgili kontrolün geçmeyeceğini doğru belirtti.

Kavram notu: Test başarısı, beklenen davranışın gerçekleşmesidir; bu davranış geçersiz girdinin reddedilmesi de olabilir. Bağımsız test değiştirme becerisi bu konuşmada ayrıca değerlendirilmedi.

### Açık sorun

Yerel editable kurulumdaki `.pth` dosyasında macOS `hidden` bayrağı tekrar gözlendi ve import başarısızlıkları yaşandı. Bayrak kaldırıldığında import çalıştı; bayrağı ekleyen işlem henüz belirlenmedi. Normal kurulumdaki test başarısı bu sorunun kalıcı olarak çözüldüğünü göstermez.

## Öğrenme denemesi — Önce değerlendir, sonra güncelle

- Uygulayan: Codex açıklama ve örnek kod sağladı; kullanıcı Python konsolunda çalıştırıp çıktıları paylaştı. Notu kullanıcının isteğiyle Codex hazırladı.
- Teknik durum: Konsol örneği doğrulandı; zaman damgasına göre gruplama veya proje koduna entegrasyon henüz uygulanmadı.
- Öğrenme gözlemi: Açıklama ve örnek kod desteğiyle üyelik sonucu ile bağlantı sayısı konsolda ayrı ayrı gözlendi. Bağımsız uygulama becerisi henüz değerlendirilmedi.

### Gözlenen sonuçlar

Başlangıçta `edge_counts = {}` idi. Aynı saniyeye ait olduğu varsayılan iki ayrı olay, aynı `laptop-01 → admin-server` bağlantısını içeriyordu. Güncellemeden önce hesaplanan `seen_before` listesi `[False, False]` oldu: her öğe bir olayın geçmişte görülüp görülmediğini ifade eder.

İki olayın ardından sözlük `{('laptop-01', 'admin-server'): 2}` oldu. Sonradan yeniden çalıştırılan üyelik kontrolleri `[True, True]` döndürdü. Bu son kontrol sayacı artırmadı; daha önce hesaplanmış `seen_before` listesi de kendiliğinden değişmedi.

### Açıklama ve düzeltme

Kullanıcı, ilk `False` sonucunu bağlantının daha önce görülmemesiyle doğru ilişkilendirdi; ancak ikinci `False` değerini bağlantı sayısına ait sandı. `edge_counts` bir sözlüktür, boolean değildir. İlk kontroldeki iki `False`, iki olayın üyelik sonuçlarıdır; güncelleme sonrasında bağlantının sayısı `2` olur. Yeniden üyelik kontrolünün `True` olması için bağlantının bir kez eklenmesi de yeterlidir.

Son kontrolde kullanıcı sözlüğü bağlantı sayısı `1` olacak şekilde yeniden atadı. Üyelik kontrolü `True`, sayaç okuması `1` döndürdü. Aynı sözlük üzerinde art arda yapılan iki üyelik kontrolü de `[True, True]` verdi. Böylece tek bir eklemenin her iki üyelik kontrolü için de yeterli olduğu konsol çıktısıyla doğrulandı.

Kavram notu: Aynı zaman damgasındaki bütün olaylar aynı geçmişle değerlendirilir; durum daha sonra topluca güncellenir. Bu örnek sıralamayı gösterir, zaman damgalarını gerçekten işleyen bir uygulamayı doğrulamaz.

## Final portföy teslimatı

Öğrenme ve eşli çalışma belgeleri final proje ağacında bulunmayacak.
TASKS.md, STATUS.md ve varsa docs/learning_log.md yerel olarak
saklanacak; yayımlanan dokümanlardaki bağlantıları kaldırılacak.
CODEX_PROJECT_START.md ve AGENTS.md de final kapsamı açısından
gözden geçirilecek. Teknik dokümantasyon ve atıflar korunacak.
