import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('/tmp/clean_spec.json', 'r', encoding='utf-8') as f:
    spec = json.load(f)

# 1. Update copyright footer outside #main
old_footer = '<footer class="min-footer">Copyright by Ersa William Lakukua PEARL Lead Wahana Visi Indonesia</footer>'
parts = html.split('<main id="main" tabindex="-1"></main>')
if len(parts) == 2:
    shell_rest = parts[1]
    if old_footer in shell_rest:
        shell_rest = shell_rest.replace(old_footer, '')
        html = parts[0] + '<main id="main" tabindex="-1"></main>' + shell_rest

# 2. Update loader HTML text
old_loader_html = '<div id="loader"><div class="spin" aria-hidden="true"></div><p data-i18n="loading">Memuat data agregat…</p></div>'
new_loader_html = '<div id="loader"><div class="spin" aria-hidden="true"></div><p id="loader-msg">Memuat pembaruan data...</p></div>'
html = html.replace(old_loader_html, new_loader_html)

if '<p data-i18n="loading">' in html:
    html = html.replace('<p data-i18n="loading">Memuat data agregat…</p>', '<p id="loader-msg">Memuat pembaruan data...</p>')

# 3. Add responsive CSS and loader CSS enhancements
responsive_marker = '/* ---------------------------------------------------------------- responsive */'
new_responsive_css = '''/* ---------------------------------------------------------------- responsive & mobile */
@media (max-width: 1000px) {
  #sidebar { transform: translateX(-100%); transition: transform .25s var(--ease-polish); box-shadow: var(--shadow-lg); }
  body.nav-open #sidebar { transform: none; }
  #shell { margin-left: 0; }
  .burger { display: inline-flex; }
  #topbar { padding: 56px 14px 10px; }
  #main { padding: 14px 14px 28px; }
  .g-2, .g-3 { grid-template-columns: 1fr; }
  .tri-row { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  html, body {
    overflow-x: hidden;
    width: 100%;
  }
  #shell {
    margin-left: 0;
    max-width: 100%;
    overflow-x: hidden;
  }
  #topbar {
    padding: 54px 12px 8px;
  }
  body.sb-collapsed #topbar {
    padding-left: 12px;
    padding-top: 54px;
  }
  #main {
    padding: 12px 10px 32px;
    max-width: 100%;
    overflow-x: hidden;
    word-break: break-word;
  }
  h1 { font-size: 1.3rem; letter-spacing: -.02em; }
  h2 { font-size: 0.95rem; margin: 18px 0 10px; }
  h3 { font-size: 0.88rem; }
  
  /* Form & filter stacking */
  .fb-grid {
    grid-template-columns: 1fr !important;
    gap: 8px;
    padding: 10px;
  }
  .fld {
    width: 100%;
  }
  
  /* Touch targets minimum 44px on mobile */
  .btn,
  .fsel,
  .icon-btn,
  .nav-item,
  .burger,
  .seg > button {
    min-height: 44px;
    display: inline-flex;
    align-items: center;
  }
  .fopt {
    min-height: 42px;
    padding: 8px 10px;
  }
  
  /* KPI summary grid responsiveness */
  .g-kpi {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 10px;
  }
  .kpi {
    padding: 12px 10px;
  }
  .kpi-val {
    font-size: 1.45rem;
  }
  .kpi-sub {
    font-size: 0.68rem;
  }

  /* Charts & layouts stack vertically */
  .g-2, .g-3 {
    grid-template-columns: 1fr !important;
    gap: 12px;
  }
  .card {
    padding: 14px 12px 12px;
  }

  /* Prevent table overflow while allowing horizontal swipe */
  .tbl-wrap {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin: 0 -4px;
  }

  /* Isolate horizontal scroll strictly to Sinyal Utama */
  .signals-scroll {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    width: 100%;
    margin-left: 0;
    margin-right: 0;
    padding-left: 2px;
    padding-right: 2px;
  }
}

@media (max-width: 480px) {
  .g-kpi {
    grid-template-columns: 1fr !important;
  }
  .kpi-val {
    font-size: 1.35rem;
  }
  .card-hd h3 {
    font-size: 0.86rem;
  }
  .bar-row {
    grid-template-columns: 1fr max-content;
    row-gap: 3px;
  }
  .bar-lab {
    grid-column: 1 / -1;
    text-align: left;
  }
  .divg-track {
    height: 16px;
  }
}

/* -------------------------------------------------- modern loader overlay */
#loader {
  position: fixed; inset: 0; background: var(--bg);
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px;
  z-index: 200;
  opacity: 1;
  visibility: visible;
  transition: opacity 0.4s var(--ease-polish), visibility 0.4s;
}
#loader.done {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
#loader p {
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--ink-2);
  margin: 0;
  letter-spacing: -0.01em;
}
.spin {
  width: 28px; height: 28px; border-radius: 50%; border: 3px solid var(--line-strong);
  border-top-color: var(--wv-orange); animation: sp .75s linear infinite;
}
.load-error-box {
  max-width: 460px;
  margin: 0 16px;
  padding: 24px 20px;
  background: var(--surface);
  border: 1px solid var(--c-crit);
  border-radius: var(--r);
  box-shadow: var(--shadow-lg);
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
.load-error-box h3 {
  color: var(--c-crit);
  font-size: 1.1rem;
  margin: 0;
}
.load-error-box p {
  font-size: 0.86rem;
  color: var(--ink-2);
  margin: 0;
  line-height: 1.5;
}
'''

if responsive_marker in html:
    end_resp = html.find('/* ---------------------------------------------------------------- card chrome */')
    html = html[:html.find(responsive_marker)] + new_responsive_css + '\n' + html[end_resp:]

# 4. Remove static embedded data and replace with dynamic fetch & parser code
old_embed_start = html.find('window.__JMA_EMBEDDED__ =')
old_embed_end = html.find('/* ==== i18n.js ====')

clean_spec_str = json.dumps(spec['indicators'])
clean_meta_str = json.dumps(spec['meta'])

new_script_header = f'''const INDICATORS_SPEC = {clean_spec_str};
const BASE_META = {clean_meta_str};

/** Google Sheets Live CSV Export Endpoint */
const GOOGLE_SHEET_CSV_URL = 'https://docs.google.com/spreadsheets/d/1YV_vssI5lI2i_ecwZG7xy3fSCn_9sJx6QB71uJ9MmeM/gviz/tq?tqx=out:csv&sheet=JMA+Flores+Earthquake+2026';

/**
 * Robust vanilla JavaScript CSV Parser
 * Correctly parses CSV text with commas, double-quoted fields,
 * escaped double-quotes (""), and newlines inside quoted strings.
 */
function parseCSV(text) {{
  const lines = [];
  let row = [''];
  let inQuotes = false;
  let i = 0;
  const len = text.length;

  while (i < len) {{
    const c = text[i];
    const next = text[i + 1];

    if (c === '"') {{
      if (inQuotes && next === '"') {{
        row[row.length - 1] += '"';
        i += 2;
        continue;
      }}
      inQuotes = !inQuotes;
      i++;
      continue;
    }}

    if (c === ',' && !inQuotes) {{
      row.push('');
      i++;
      continue;
    }}

    if ((c === '\\r' || c === '\\n') && !inQuotes) {{
      if (c === '\\r' && next === '\\n') i++;
      if (row.length > 1 || row[0] !== '') {{
        lines.push(row);
      }}
      row = [''];
      i++;
      continue;
    }}

    row[row.length - 1] += c;
    i++;
  }}

  if (row.length > 1 || row[0] !== '') {{
    lines.push(row);
  }}

  if (lines.length < 2) return [];

  const headers = lines[0].map(h => h.trim());
  const objects = [];
  for (let r = 1; r < lines.length; r++) {{
    const vals = lines[r];
    const obj = {{}};
    for (let c = 0; c < headers.length; c++) {{
      obj[headers[c]] = vals[c] !== undefined ? vals[c].trim() : '';
    }}
    objects.push(obj);
  }}
  return objects;
}}

const GROUP_CODE_MAP = {{
  'Rumah Tangga': 'HH',
  'Pedagang/Pembeli/Distributor': 'TRD',
  'Pemerintah/Lembaga': 'GOV',
  'Penyedia Layanan': 'FSP',
  'NGO/OMS': 'NGO'
}};

function cleanKecamatan(kab, kec) {{
  kec = (kec || '').trim();
  if (kab === 'Manggarai' && kec.toLowerCase() === 'cibal barat') return 'Cibal Barat';
  return kec;
}}

/**
 * Aggregates raw survey row objects into the dashboard data cube (DATA.cells)
 * and generates live metadata (DATA.meta)
 */
function processRowsToData(rows, indicatorsList, metaTemplate) {{
  const cellsMap = new Map();

  function getCell(L, g, kab, kec, d, o, m, cats) {{
    const cKey = cats.slice().sort().join('|');
    const key = [L, g, kab, kec, d, o, m, cKey].join(':::');
    let cell = cellsMap.get(key);
    if (!cell) {{
      cell = {{
        L, g, kab, kec, d, o, m,
        c: cats.slice().sort(),
        n: 0,
        v: {{}},
        num: {{}},
        pair: {{}}
      }};
      cellsMap.set(key, cell);
    }}
    return cell;
  }}

  const indsByGroup = {{}};
  for (const ind of indicatorsList) {{
    if (!indsByGroup[ind.group]) indsByGroup[ind.group] = [];
    indsByGroup[ind.group].push(ind);
  }}

  const recordsByGroup = {{ HH: 0, TRD: 0, GOV: 0, FSP: 0, NGO: 0 }};
  const kabSet = new Set();
  const kabKecMap = {{}};
  const orgSet = new Set();
  const methodSet = new Set();
  const catSet = new Set();
  const dates = [];

  for (const r of rows) {{
    const rawGrp = r['U01. Kelompok Responden'];
    const g = GROUP_CODE_MAP[rawGrp];
    if (!g) continue;

    recordsByGroup[g] = (recordsByGroup[g] || 0) + 1;

    const kab = (r['U08. Kabupaten/Kota'] || '').trim();
    const rawKec = (r['U09. Kecamatan'] || '').trim();
    const kec = cleanKecamatan(kab, rawKec);
    const d = (r['U04. Tanggal Wawancara'] || '').trim();
    const o = (r['U02. Organisasi Pengambil Data'] || '').trim();
    const m = (r['U05. Metode Wawancara'] || '').trim();

    if (kab) kabSet.add(kab);
    if (kab && kec) {{
      if (!kabKecMap[kab]) kabKecMap[kab] = new Set();
      kabKecMap[kab].add(kec);
    }}
    if (o) orgSet.add(o);
    if (m) methodSet.add(m);
    if (d) dates.push(d);

    const cats = [];
    const catStr = (r['U11. Produk/Layanan Utama yang Dikaji'] || '').trim();
    if (catStr) {{
      cats.push(catStr);
      catSet.add(catStr);
    }}

    const cell0 = getCell(0, g, kab, kec, d, o, m, cats);
    cell0.n += 1;
    const cell1 = getCell(1, g, kab, '', d, o, m, cats);
    cell1.n += 1;

    const groupInds = indsByGroup[g] || [];
    for (const ind of groupInds) {{
      const target = ind.sensitive ? cell1 : cell0;
      const kind = ind.kind;
      const id = ind.id;

      if (kind === 'cat') {{
        const src = ind.source_fields[0];
        const val = (r[src] || '').trim();
        const opts = ind.options;
        const optIdx = opts.indexOf(val);
        if (optIdx !== -1) {{
          if (!target.v[id]) target.v[id] = new Array(opts.length).fill(0);
          target.v[id][optIdx] += 1;
        }}
      }} else if (kind === 'multi') {{
        const prefix = ind.source_fields[0].replace('/*', '');
        const opts = ind.options;
        let ans = false;
        const matched = new Array(opts.length).fill(0);
        for (let oi = 0; oi < opts.length; oi++) {{
          const opt = opts[oi];
          const col = prefix + '/' + opt;
          if (r[col] === '1' || (r[prefix] && r[prefix].includes(opt))) {{
            matched[oi] = 1;
            ans = true;
          }}
        }}
        if (ans || (r[prefix] && r[prefix].trim().length > 0)) {{
          if (!target.v[id]) target.v[id] = new Array(opts.length + 1).fill(0);
          for (let oi = 0; oi < opts.length; oi++) {{
            target.v[id][oi] += matched[oi];
          }}
          target.v[id][opts.length] += 1;
        }}
      }} else if (kind === 'num') {{
        const src = ind.source_fields[0];
        const valStr = (r[src] || '').trim();
        if (valStr) {{
          const numVal = parseFloat(valStr);
          if (!isNaN(numVal) && numVal >= 0) {{
            if (!target.num[id]) target.num[id] = [];
            target.num[id].push(numVal);
          }}
        }}
      }} else if (kind === 'pair') {{
        const [f1, f2] = ind.source_fields;
        const v1Str = (r[f1] || '').trim();
        const v2Str = (r[f2] || '').trim();
        if (v1Str && v2Str) {{
          const v1 = parseFloat(v1Str);
          const v2 = parseFloat(v2Str);
          if (!isNaN(v1) && !isNaN(v2) && v1 > 0 && v2 >= 0) {{
            const ratio = Math.round((v2 / v1) * 10000) / 10000;
            if (!target.pair[id]) target.pair[id] = [];
            target.pair[id].push(ratio);
          }}
        }}
      }}
    }}
  }}

  dates.sort();
  const sortedKabKec = {{}};
  for (const k of Array.from(kabSet).sort()) {{
    sortedKabKec[k] = Array.from(kabKecMap[k] || []).sort();
  }}

  const meta = {{
    ...metaTemplate,
    total_records: rows.length,
    records_by_group: recordsByGroup,
    kabupaten: Array.from(kabSet).sort(),
    kabupaten_kecamatan: sortedKabKec,
    kecamatan_count: Object.values(sortedKabKec).reduce((acc, l) => acc + l.length, 0),
    organisations: Array.from(orgSet).sort(),
    methods: Array.from(methodSet).sort(),
    product_categories: Array.from(catSet),
    date_min: dates[0] || '2026-08-26',
    date_max: dates[dates.length - 1] || '2026-09-14',
    cube_cells: cellsMap.size
  }};

  const indMap = {{}};
  for (const i of indicatorsList) indMap[i.id] = i;

  return {{
    meta,
    cells: Array.from(cellsMap.values()),
    ind: indMap,
    formulas: {{
      cat: 'persen_opsi = jumlah_responden_memilih_opsi / jumlah_jawaban_valid x 100',
      multi: 'persen_opsi = jumlah_responden_memilih_opsi / jumlah_responden_menjawab_blok x 100 (total dapat > 100%)',
      num: 'median dan IQR dari nilai valid dalam jendela plausibel; rata-rata tidak digunakan',
      pair: 'rasio = nilai_saat_ini / nilai_dasar (per responden); persen_perubahan = (rasio - 1) x 100; arah = naik jika rasio > 1, tetap jika = 1, turun jika < 1'
    }}
  }};
}}
</script>
<script>
'''

html = html[:old_embed_start] + new_script_header + html[old_embed_end:]

# 5. Replace loadData() in data.js
old_loaddata_start = html.find('async function loadData() {')
old_loaddata_end = html.find('/* ---------------------------------------------------------------- filtering */')

new_loaddata = '''async function loadData() {
  const resp = await fetch(GOOGLE_SHEET_CSV_URL);
  if (!resp.ok) {
    throw new Error(`Gagal mengambil data spreadsheet (HTTP ${resp.status})`);
  }
  const csvText = await resp.text();
  const rows = parseCSV(csvText);
  if (!rows || !rows.length) {
    throw new Error('Data spreadsheet kosong atau tidak dapat diuraikan');
  }
  const processed = processRowsToData(rows, INDICATORS_SPEC, BASE_META);
  DATA.meta = processed.meta;
  DATA.cells = processed.cells;
  DATA.ind = processed.ind;
  DATA.formulas = processed.formulas;
  DATA.ready = true;
}

'''

html = html[:old_loaddata_start] + new_loaddata + html[old_loaddata_end:]

# 6. Replace boot() in boot section
old_boot_start = html.find('(async function boot() {')
new_boot = '''(async function boot() {
  initTheme();

  const showLoadError = (err) => {
    const loader = document.getElementById('loader');
    if (loader) {
      loader.classList.remove('done');
      loader.style.opacity = '1';
      loader.style.visibility = 'visible';
      loader.style.display = 'flex';
      const msg = err && err.message ? err.message : String(err);
      loader.innerHTML = `
        <div class="load-error-box">
          <svg viewBox="0 0 24 24" class="ic" style="width:38px;height:38px;color:var(--c-crit)" aria-hidden="true">
            <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>
          </svg>
          <h3>${LANG === 'en' ? 'Failed to Load Sheet Data' : 'Gagal Memuat Data Spreadsheet'}</h3>
          <p>${esc(msg)}</p>
          <p style="font-size:0.78rem;color:var(--ink-3);margin:0">
            ${LANG === 'en' ? 'Please ensure you are online and that the Google Sheet is accessible.' : 'Pastikan Anda terhubung ke internet dan spreadsheet Google Sheet dapat diakses.'}
          </p>
          <button type="button" class="btn btn-primary" onclick="location.reload()" style="margin-top:6px">
            ${LANG === 'en' ? 'Retry' : 'Muat Ulang'}
          </button>
        </div>`;
    }
  };

  try {
    await loadData();
  } catch (e) {
    console.error('Data initialization failed:', e);
    showLoadError(e);
    return;
  }

  buildNav();
  buildFilters();
  bindCardActions();
  renderChips();
  applyStaticI18n();
  render();
  initChrome();
  initCovers();

  document.getElementById('btn-reset').addEventListener('click', resetFilters);
  document.getElementById('btn-csv').addEventListener('click', downloadCSV);
  document.getElementById('btn-theme').addEventListener('click', () => {
    const root = document.documentElement;
    const dark = root.dataset.theme === 'dark';
    root.classList.add('theming');
    root.dataset.theme = dark ? 'light' : 'dark';
    localStorage.setItem('jma-theme', dark ? 'light' : 'dark');
    setThemeIcon();
    window.setTimeout(() => root.classList.remove('theming'), 340);
  });
  document.querySelectorAll('.seg [data-lang]').forEach(b => {
    b.addEventListener('click', () => setLang(b.dataset.lang));
  });
  document.getElementById('burger').addEventListener('click', e => {
    if (document.body.classList.contains('sb-collapsed')) { window.jmaSetSb(false); return; }
    const open = document.body.classList.toggle('nav-open');
    e.currentTarget.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', () => closePanels(null));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && OPEN_PANEL) {
      const b = document.querySelector(`.fsel[data-open=\"${OPEN_PANEL}\"]`);
      closePanels(null);
      if (b) b.focus();
    }
  });
  window.addEventListener('hashchange', () => {
    const id = location.hash.replace('#', '');
    if (id && id !== ACTIVE) go(id);
  });

  // Fade out loader smoothly
  const loader = document.getElementById('loader');
  if (loader) {
    loader.classList.add('done');
    setTimeout(() => { loader.style.display = 'none'; }, 420);
  }
})();
'''

old_boot_end = html.rfind('})();') + 5
html = html[:old_boot_start] + new_boot + html[old_boot_end:]

with open('/tmp/new_index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('SUCCESS: Created /tmp/new_index.html with length', len(html))
