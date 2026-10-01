import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de pantalla completa
st.set_page_config(
    page_title="TutorU | Portal Oficial",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Reset de márgenes de Streamlit
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Código de la Interfaz con los ajustes solicitados
HTML_APP = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: { sans: ['"Plus Jakarta Sans"', 'sans-serif'] },
          colors: {
            ucuenca: {
              navy: '#0C2340',
              navydark: '#071629',
              navylight: '#183B6B',
              wine: '#8B1538',
              winedark: '#6E0F2B',
              winelight: '#A51D45',
              surface: '#F8FAFC',
            }
          },
          boxShadow: {
            'card-hover': '0 14px 30px -8px rgba(12, 35, 64, 0.12), 0 4px 10px -4px rgba(139, 21, 56, 0.08)',
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #F8FAFC; color: #1E293B; }
    .glass-nav { background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(12px); }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased bg-slate-50 text-slate-800">

  <!-- Top Ribbon Oficial -->
  <header class="bg-ucuenca-navydark text-xs text-slate-300 border-b border-white/10 px-4 py-1.5 hidden md:block">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-4">
        <span class="inline-flex items-center gap-1.5 text-slate-200">
          <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-400"></i>
          <span>Ciclo Académico 2026 – 2027</span>
        </span>
        <span class="text-white/30">•</span>
        <span class="text-slate-300">Campus Central & Bibliotecas</span>
      </div>
      <div class="flex items-center gap-5">
        <span class="flex items-center gap-1 text-slate-200">
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-400"></i> Tutores 100% Verificados por Récord Académico
        </span>
      </div>
    </div>
  </header>

  <!-- Navbar Principal: SIN el texto 'Universidad de Cuenca' debajo de TutorU -->
  <nav class="sticky top-0 z-40 glass-nav border-b border-slate-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- Identidad Visual limpia sin subtítulo -->
        <div class="flex items-center gap-3 cursor-pointer" onclick="setActiveTab('explore')">
          <div class="relative flex items-center justify-center w-11 h-11 rounded-xl bg-gradient-to-br from-ucuenca-wine to-ucuenca-winedark text-white shadow-md">
            <i data-lucide="graduation-cap" class="w-6 h-6"></i>
            <span class="absolute -bottom-1 -right-1 w-4 h-4 bg-ucuenca-navy rounded-full border-2 border-white flex items-center justify-center text-[9px] font-bold text-white">U</span>
          </div>
          <div class="flex items-baseline gap-1.5">
            <span class="text-2xl font-black tracking-tight text-ucuenca-navy">Tutor<span class="text-ucuenca-wine">U</span></span>
            <span class="text-[10px] font-bold tracking-widest text-white uppercase bg-ucuenca-navy px-1.5 py-0.5 rounded">OFICIAL</span>
          </div>
        </div>

        <!-- Botones de Navegación -->
        <div class="hidden lg:flex items-center bg-slate-100 p-1.5 rounded-2xl border border-slate-200/80 gap-1">
          <button id="nav-btn-explore" onclick="setActiveTab('explore')" class="px-3.5 py-2 text-xs font-bold rounded-xl transition-all flex items-center gap-1.5 bg-white text-ucuenca-navy shadow-sm">
            <i data-lucide="compass" class="w-4 h-4 text-ucuenca-wine"></i>
            Explorar Tutores
          </button>
          
          <button id="nav-btn-community" onclick="setActiveTab('community')" class="px-3.5 py-2 text-xs font-semibold rounded-xl text-slate-600 hover:text-ucuenca-navy transition-all flex items-center gap-1.5">
            <i data-lucide="message-square" class="w-4 h-4"></i>
            Muro Comunitario
          </button>

          <!-- Sección propia "Pedir Ayuda" -->
          <button id="nav-btn-request" onclick="setActiveTab('request')" class="px-3.5 py-2 text-xs font-bold rounded-xl text-white bg-ucuenca-wine hover:bg-ucuenca-winedark transition-all flex items-center gap-1.5 shadow-sm">
            <i data-lucide="plus-circle" class="w-4 h-4 text-amber-300"></i>
            Pedir Ayuda
          </button>

          <button id="nav-btn-betutor" onclick="setActiveTab('betutor')" class="px-3.5 py-2 text-xs font-semibold rounded-xl text-slate-600 hover:text-ucuenca-navy transition-all flex items-center gap-1.5">
            <i data-lucide="award" class="w-4 h-4"></i>
            Quiero Ser Tutor
          </button>

          <button id="nav-btn-classes" onclick="setActiveTab('classes')" class="px-3.5 py-2 text-xs font-semibold rounded-xl text-slate-600 hover:text-ucuenca-navy transition-all flex items-center gap-1.5 relative">
            <i data-lucide="calendar" class="w-4 h-4"></i>
            Mis Clases
            <span id="badge-clases-count" class="ml-1 px-1.5 py-0.2 bg-ucuenca-navy text-white text-[10px] font-bold rounded-full">1</span>
          </button>
        </div>

        <!-- Billetera y Perfil -->
        <div class="flex items-center gap-3">
          <div class="flex items-center bg-slate-50 border border-slate-200 rounded-xl p-1 pr-3 gap-2 shadow-sm">
            <button onclick="openDepositModal()" class="w-7 h-7 rounded-lg bg-ucuenca-wine/10 text-ucuenca-wine hover:bg-ucuenca-wine hover:text-white flex items-center justify-center transition" title="Recargar">
              <i data-lucide="wallet" class="w-4 h-4"></i>
            </button>
            <div class="flex flex-col">
              <span class="text-[9px] uppercase tracking-wider text-slate-500 font-semibold leading-none">Mi Saldo</span>
              <span id="user-balance-display" class="text-sm font-black text-ucuenca-navy leading-none mt-0.5">$24.50</span>
            </div>
            <button onclick="openDepositModal()" class="w-5 h-5 rounded-full bg-slate-200 hover:bg-ucuenca-wine hover:text-white flex items-center justify-center text-xs font-bold text-slate-600 transition">+</button>
          </div>

          <div class="flex items-center gap-2.5 pl-2 border-l border-slate-200">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&h=120&q=80" class="w-10 h-10 rounded-xl object-cover ring-2 ring-ucuenca-navy/20 shadow-sm">
            <div class="hidden md:flex flex-col text-left">
              <div class="flex items-center gap-1">
                <span class="text-xs font-bold text-ucuenca-navy">Juanita Perez</span>
                <i data-lucide="check-circle" class="w-3 h-3 text-ucuenca-wine"></i>
              </div>
              <span class="text-[10px] font-semibold text-slate-500">Admin. Empresas</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </nav>

  <!-- Hero Banner Azul Marino: SOLO LOGO BLANCO UCUENCA Y MARCA DE AGUA UC -->
  <section class="relative bg-gradient-to-r from-ucuenca-navy via-[#102d52] to-ucuenca-navydark text-white overflow-hidden py-10 px-4 sm:px-6 lg:px-8 border-b border-ucuenca-navylight/30">
    <!-- Marca de agua circular UC conservada en el fondo -->
    <div class="absolute -right-12 -bottom-16 opacity-10 pointer-events-none select-none">
      <div class="w-80 h-80 rounded-full border-[18px] border-white flex items-center justify-center">
        <span class="text-8xl font-black">UC</span>
      </div>
    </div>

    <!-- Contenedor donde antes iban las letras: Ahora únicamente el logo blanco UCUENCA -->
    <div class="max-w-7xl mx-auto relative z-10 flex items-center justify-start py-2">
      <h1 class="text-5xl sm:text-6xl md:text-7xl font-black tracking-tight text-white select-none uppercase font-['Plus_Jakarta_Sans'] leading-none">
        UCUENCA
      </h1>
    </div>
  </section>

  <!-- Contenedor Principal de Vistas -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">

    <!-- 1. VISTA: EXPLORAR TUTORES -->
    <div id="view-explore" class="space-y-6">
      <div class="bg-white rounded-3xl p-5 shadow-sm border border-slate-200/90 space-y-4">
        <div class="flex flex-col lg:flex-row gap-3">
          <div class="relative flex-1">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-400">
              <i data-lucide="search" class="w-5 h-5 text-ucuenca-wine"></i>
            </div>
            <input 
              type="text" 
              id="search-input" 
              placeholder="Buscar por materia, profesor o tema (ej. Costos, Estructuras, Cálculo)..."
              class="w-full pl-11 pr-10 py-3.5 bg-slate-50 text-sm font-medium text-slate-800 rounded-2xl border border-slate-200 focus:outline-none focus:border-ucuenca-wine"
              oninput="handleSearch()"
            >
          </div>

          <div class="relative lg:w-80">
            <select 
              id="faculty-select" 
              onchange="handleSearch()" 
              class="w-full px-4 py-3.5 bg-slate-50 text-sm font-semibold text-ucuenca-navy rounded-2xl border border-slate-200 focus:outline-none"
            >
              <option value="all">Todas las Facultades</option>
              <option value="ingenieria">Facultad de Ingeniería</option>
              <option value="economicas">Ciencias Económicas y Adm.</option>
              <option value="medicas">Ciencias Médicas</option>
              <option value="jurisprudencia">Jurisprudencia y Cs. Políticas</option>
            </select>
          </div>
        </div>

        <div class="flex items-center justify-between flex-wrap gap-2 pt-1 border-t border-slate-100">
          <div class="flex items-center gap-1.5 flex-wrap text-xs">
            <span class="text-xs font-bold text-slate-600 mr-1">Filtros:</span>
            <button onclick="setChipFilter('all')" class="chip-btn px-3.5 py-1.5 rounded-xl font-bold bg-ucuenca-wine text-white">Todos</button>
            <button onclick="setChipFilter('virtual')" class="chip-btn px-3.5 py-1.5 rounded-xl font-medium bg-slate-100 text-slate-700">Virtual (Meet)</button>
            <button onclick="setChipFilter('campus-central')" class="chip-btn px-3.5 py-1.5 rounded-xl font-medium bg-slate-100 text-slate-700">Campus Central</button>
            <button onclick="setChipFilter('biblioteca')" class="chip-btn px-3.5 py-1.5 rounded-xl font-medium bg-slate-100 text-slate-700">Biblioteca Central</button>
          </div>
          <div class="text-xs text-slate-600 font-semibold">
            Mostrando <span id="tutor-count-badge" class="font-bold text-ucuenca-wine text-sm">6</span> tutores
          </div>
        </div>
      </div>

      <div id="tutors-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>
    </div>

    <!-- 2. VISTA DEDICADA: PEDIR AYUDA -->
    <div id="view-request" class="hidden space-y-6">
      <div class="bg-gradient-to-r from-ucuenca-wine to-ucuenca-winedark rounded-3xl p-6 text-white shadow-md flex items-center justify-between">
        <div>
          <span class="text-[10px] font-bold tracking-wider uppercase px-2.5 py-1 bg-white/20 rounded-md text-amber-300">Publicación Rápida</span>
          <h2 class="text-2xl font-black mt-1">Solicitar Apoyo Académico</h2>
          <p class="text-xs text-rose-100 mt-0.5">Publica el ejercicio o tema en el que tienes dudas y define cuánto deseas pagar.</p>
        </div>
        <div class="hidden sm:flex w-12 h-12 rounded-2xl bg-white/10 items-center justify-center">
          <i data-lucide="help-circle" class="w-6 h-6 text-amber-300"></i>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div class="lg:col-span-7 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
          <h3 class="text-base font-extrabold text-ucuenca-navy flex items-center gap-2">
            <i data-lucide="edit-3" class="w-4 h-4 text-ucuenca-wine"></i> Formulario de tu Requerimiento
          </h3>

          <form onsubmit="handleCrearSolicitud(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Materia</label>
              <input type="text" id="req-materia" required placeholder="Ej. Costos I, Álgebra Lineal..." class="w-full text-xs p-3.5 rounded-xl border border-slate-200 bg-slate-50 focus:border-ucuenca-wine">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Facultad</label>
                <select id="req-facultad" class="w-full text-xs p-3.5 rounded-xl border border-slate-200 bg-slate-50 font-semibold text-slate-700">
                  <option>Ciencias Económicas y Adm.</option>
                  <option>Facultad de Ingeniería</option>
                  <option>Ciencias Médicas</option>
                  <option>Jurisprudencia</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Presupuesto ($ USD)</label>
                <input type="number" id="req-paga" step="0.50" min="2.00" value="5.00" required class="w-full text-xs p-3.5 rounded-xl border border-slate-200 bg-slate-50 font-bold text-ucuenca-wine">
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Plazo Máximo</label>
              <input type="text" id="req-plazo" required placeholder="Ej. Hoy hasta las 19:00" class="w-full text-xs p-3.5 rounded-xl border border-slate-200 bg-slate-50">
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Descripción del Problema o Taller</label>
              <textarea id="req-desc" rows="3" required placeholder="Explica detalladamente qué ejercicios o temas necesitas revisar..." class="w-full text-xs p-3 rounded-xl border border-slate-200 bg-slate-50"></textarea>
            </div>

            <button type="submit" class="w-full py-3.5 rounded-xl bg-ucuenca-wine hover:bg-ucuenca-winedark text-white font-bold text-xs shadow-md transition flex items-center justify-center gap-2">
              <i data-lucide="send" class="w-4 h-4"></i> Publicar Solicitud en el Muro
            </button>
          </form>
        </div>

        <div class="lg:col-span-5 space-y-4">
          <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-3">
            <h3 class="text-sm font-extrabold text-ucuenca-navy flex items-center justify-between">
              <span>📋 Mis Solicitudes Publicadas</span>
              <span id="user-req-count" class="text-xs px-2 py-0.5 bg-slate-100 rounded-full font-bold text-ucuenca-wine">1</span>
            </h3>
            <p class="text-[11px] text-slate-500">Monitorea tus dudas publicadas y los tutores que se han postulado.</p>
            <div id="mis-solicitudes-container" class="space-y-3 pt-2"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. VISTA: MURO COMUNITARIO -->
    <div id="view-community" class="hidden space-y-6">
      <div class="bg-gradient-to-r from-ucuenca-navy to-ucuenca-navylight rounded-3xl p-6 text-white shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <span class="text-[10px] font-bold tracking-wider uppercase px-2.5 py-1 bg-white/15 rounded-md text-amber-300">Muro Estudiantil</span>
          <h2 class="text-2xl font-black mt-1">Dudas y Talleres de Compañeros</h2>
          <p class="text-xs text-slate-200 mt-0.5">Postúlate para resolver las dudas de otros alumnos y cobrar la recompensa.</p>
        </div>
        <button onclick="setActiveTab('request')" class="px-5 py-2.5 rounded-xl bg-ucuenca-wine hover:bg-ucuenca-winedark text-white text-xs font-bold transition flex items-center gap-2">
          <i data-lucide="plus" class="w-4 h-4"></i> Publicar Mi Duda
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="community-feed-grid"></div>
    </div>

    <!-- 4. VISTA: QUIERO SER TUTOR -->
    <div id="view-betutor" class="hidden space-y-6">
      <div class="max-w-2xl mx-auto bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-5">
        <div class="text-center space-y-1.5">
          <div class="w-12 h-12 rounded-2xl bg-ucuenca-wine/10 text-ucuenca-wine flex items-center justify-center mx-auto">
            <i data-lucide="award" class="w-7 h-7"></i>
          </div>
          <h2 class="text-xl font-black text-ucuenca-navy">Registro de Tutor Oficial</h2>
          <p class="text-xs text-slate-500">Gana dinero en tus horas libres dentro del campus.</p>
        </div>

        <form onsubmit="handlePostularTutor(event)" class="space-y-4 text-xs">
          <div>
            <label class="block font-bold text-slate-700 uppercase mb-1">Materia a Dictar</label>
            <input type="text" id="tutor-reg-materia" required placeholder="Ej. Macroeconomía I" class="w-full p-3 rounded-xl border border-slate-200 bg-slate-50">
          </div>
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block font-bold text-slate-700 uppercase mb-1">Nota Obtenida</label>
              <input type="text" id="tutor-reg-nota" required placeholder="Ej. 95/100" class="w-full p-3 rounded-xl border border-slate-200 bg-slate-50">
            </div>
            <div>
              <label class="block font-bold text-slate-700 uppercase mb-1">Docente Anterior</label>
              <input type="text" id="tutor-reg-docente" required placeholder="Ej. Econ. Vázquez" class="w-full p-3 rounded-xl border border-slate-200 bg-slate-50">
            </div>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block font-bold text-slate-700 uppercase mb-1">Tarifa por Hora ($)</label>
              <input type="number" id="tutor-reg-tarifa" step="0.50" min="3.00" value="4.50" class="w-full p-3 rounded-xl border border-slate-200 bg-slate-50 font-bold text-ucuenca-wine">
            </div>
            <div>
              <label class="block font-bold text-slate-700 uppercase mb-1">Modalidad</label>
              <select id="tutor-reg-modalidad" class="w-full p-3 rounded-xl border border-slate-200 bg-slate-50 font-semibold">
                <option value="virtual">Virtual (Meet)</option>
                <option value="biblioteca">Biblioteca Central</option>
                <option value="campus-central">Campus Central</option>
              </select>
            </div>
          </div>
          <button type="submit" class="w-full py-3.5 rounded-xl bg-ucuenca-wine hover:bg-ucuenca-winedark text-white font-bold transition">
            Validar y Publicar mi Perfil
          </button>
        </form>
      </div>
    </div>

    <!-- 5. VISTA: MIS CLASES -->
    <div id="view-classes" class="hidden space-y-6">
      <div class="flex items-center justify-between bg-white p-6 rounded-3xl border border-slate-200 shadow-sm">
        <div>
          <h2 class="text-xl font-black text-ucuenca-navy">Mis Tutorías Programadas</h2>
          <p class="text-xs text-slate-500">Sesiones aseguradas en garantía institucional.</p>
        </div>
        <button onclick="setActiveTab('explore')" class="px-4 py-2 rounded-xl bg-ucuenca-wine text-white text-xs font-bold hover:bg-ucuenca-winedark transition flex items-center gap-1.5">
          <i data-lucide="plus" class="w-4 h-4"></i> Agendar Otra
        </button>
      </div>
      <div id="booked-classes-list" class="space-y-4"></div>
    </div>

  </main>

  <!-- Modal de Reserva -->
  <div id="booking-modal" class="fixed inset-0 z-50 hidden bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 relative">
      <button onclick="closeBookingModal()" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 text-slate-500 flex items-center justify-center">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>
      <div class="flex items-center gap-3.5 pb-4 border-b border-slate-100">
        <img id="modal-tutor-avatar" src="" class="w-12 h-12 rounded-2xl object-cover ring-2 ring-ucuenca-wine/30">
        <div>
          <h3 id="modal-tutor-name" class="text-base font-black text-ucuenca-navy">Tutor</h3>
          <p id="modal-tutor-course" class="text-xs font-semibold text-ucuenca-wine">Materia</p>
          <p id="modal-tutor-merit" class="text-[11px] text-slate-500">Nota</p>
        </div>
      </div>
      <div class="py-4 space-y-2 text-xs">
        <div class="flex justify-between">
          <span class="text-slate-600">Tarifa por 1 hora:</span>
          <span id="modal-fee-display" class="font-bold text-ucuenca-navy">$4.50</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-600">Tu saldo disponible:</span>
          <span id="modal-balance-display" class="font-semibold text-emerald-600">$24.50</span>
        </div>
      </div>
      <div class="flex items-center gap-2 pt-2">
        <button onclick="closeBookingModal()" class="w-1/3 py-3 rounded-xl border font-bold text-xs">Cancelar</button>
        <button onclick="confirmBooking()" class="w-2/3 py-3 rounded-xl bg-ucuenca-wine text-white font-bold text-xs shadow-md">Confirmar Reserva</button>
      </div>
    </div>
  </div>

  <!-- Modal de Recarga -->
  <div id="deposit-modal" class="fixed inset-0 z-50 hidden bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border relative text-center">
      <button onclick="closeDepositModal()" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 text-slate-500 flex items-center justify-center">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>
      <h3 class="text-base font-black text-ucuenca-navy mb-2">Recargar Saldo</h3>
      <div class="space-y-3 text-xs">
        <input type="number" id="deposit-val" value="10.00" class="w-full text-center text-lg font-black text-ucuenca-navy p-2 border rounded-xl">
        <button onclick="executeDeposit()" class="w-full py-3 rounded-xl bg-ucuenca-navy text-white font-bold">Acreditar a Billetera</button>
      </div>
    </div>
  </div>

  <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <script>
    let userBalance = 24.50;
    let selectedTutor = null;

    const tutorsData = [
      {
        id: 1,
        name: "Mateo Cárdenas",
        facultyKey: "ingenieria",
        facultyLabel: "Facultad de Ingeniería",
        course: "Estructuras de Datos y Algoritmos",
        teacher: "Ing. Morales",
        score: "97/100",
        rating: 4.9,
        reviewsCount: 19,
        hourlyRate: 4.50,
        modality: "virtual",
        location: "Virtual (Google Meet)",
        avatar: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Árboles AVL", "Grafos", "Python / C++"]
      },
      {
        id: 2,
        name: "Paola Ordóñez",
        facultyKey: "economicas",
        facultyLabel: "Ciencias Económicas y Adm.",
        course: "Contabilidad de Costos",
        teacher: "Econ. Vázquez",
        score: "95/100",
        rating: 5.0,
        reviewsCount: 28,
        hourlyRate: 4.00,
        modality: "biblioteca",
        location: "Presencial (Biblioteca Central)",
        avatar: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Costos por Órdenes", "Kardex", "Puntos de Equilibrio"]
      },
      {
        id: 3,
        name: "Esteban Vivar",
        facultyKey: "economicas",
        facultyLabel: "Ciencias Económicas y Adm.",
        course: "Microeconomía Intermedia",
        teacher: "Dra. Pesántez",
        score: "92/100",
        rating: 4.8,
        reviewsCount: 12,
        hourlyRate: 5.00,
        modality: "campus-central",
        location: "Presencial (Campus Central)",
        avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Curvas Indiferencia", "Monopolio", "Teoría Juegos"]
      },
      {
        id: 4,
        name: "Valeria Montesdeoca",
        facultyKey: "ingenieria",
        facultyLabel: "Facultad de Ingeniería",
        course: "Cálculo en Una Variable",
        teacher: "Ing. Palacios",
        score: "99/100",
        rating: 5.0,
        reviewsCount: 42,
        hourlyRate: 4.25,
        modality: "virtual",
        location: "Virtual (Google Meet)",
        avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Integrales", "Series Taylor"]
      },
      {
        id: 5,
        name: "Carlos Cordero",
        facultyKey: "medicas",
        facultyLabel: "Ciencias Médicas",
        course: "Anatomía Humana Descriptiva",
        teacher: "Dr. Orellana",
        score: "96/100",
        rating: 4.9,
        reviewsCount: 31,
        hourlyRate: 5.50,
        modality: "campus-central",
        location: "Presencial (Campus Paraíso)",
        avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Neuroanatomía", "Atlas 3D"]
      },
      {
        id: 6,
        name: "Sofía Albarracín",
        facultyKey: "jurisprudencia",
        facultyLabel: "Jurisprudencia",
        course: "Derecho Constitucional",
        teacher: "Dr. Benalcázar",
        score: "94/100",
        rating: 4.9,
        reviewsCount: 17,
        hourlyRate: 4.50,
        modality: "biblioteca",
        location: "Presencial (Biblioteca Central)",
        avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Acción Protección", "Garantías"]
      }
    ];

    let communityPosts = [
      {
        id: 1,
        author: "Felipe Astudillo",
        course: "Cálculo III",
        text: "¿Alguien que domine el Teorema de Stokes para el taller del Ing. Palacios?",
        bounty: 5.00
      },
      {
        id: 2,
        author: "Camila Pesántez",
        course: "Contabilidad de Costos",
        text: "¿Alguien con apuntes del método de costos por procesos del Dr. Vázquez?",
        bounty: 6.00
      }
    ];

    let misSolicitudes = [
      {
        id: 101,
        materia: "Costos I",
        desc: "Necesito explicación de la tasa predeterminada de CIF por órdenes.",
        paga: 5.00,
        plazo: "Viernes 11:00",
        postulantes: 2
      }
    ];

    let bookedClasses = [
      {
        id: 201,
        tutorName: "Mateo Cárdenas",
        course: "Estructuras de Datos y Algoritmos",
        date: "Hoy, 17:00 - 18:00",
        modality: "Virtual (Google Meet)",
        meetLink: "https://meet.google.com/new",
        fee: 4.50,
        avatar: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=120&h=120&q=80"
      }
    ];

    function renderTutors(list) {
      const container = document.getElementById('tutors-grid');
      document.getElementById('tutor-count-badge').textContent = list.length;

      container.innerHTML = list.map(tutor => {
        let modIcon = tutor.modality === 'virtual' ? 'video' : (tutor.modality === 'biblioteca' ? 'book-marked' : 'map-pin');
        let modColor = tutor.modality === 'virtual' ? 'text-blue-600 bg-blue-50' : 'text-rose-600 bg-rose-50';

        return `
          <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm hover:shadow-card-hover transition-all flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between gap-2 mb-3">
                <span class="text-[11px] font-bold text-ucuenca-wine bg-ucuenca-wine/10 px-2.5 py-1 rounded-lg truncate max-w-[180px]">
                  ${tutor.facultyLabel}
                </span>
                <span class="text-[11px] font-semibold flex items-center gap-1 px-2.5 py-1 rounded-lg ${modColor}">
                  <i data-lucide="${modIcon}" class="w-3.5 h-3.5"></i> ${tutor.location}
                </span>
              </div>

              <div class="flex items-center gap-3.5 mb-3.5">
                <img src="${tutor.avatar}" class="w-14 h-14 rounded-2xl object-cover ring-2 ring-ucuenca-navy/15">
                <div>
                  <h3 class="text-base font-extrabold text-ucuenca-navy">${tutor.name}</h3>
                  <div class="flex items-center gap-1.5 mt-0.5 text-xs">
                    <span class="text-amber-500 font-bold">★ ${tutor.rating.toFixed(1)}</span>
                    <span class="text-slate-400">(${tutor.reviewsCount} reseñas)</span>
                  </div>
                </div>
              </div>

              <h4 class="text-sm font-black text-slate-900 leading-snug mb-2">${tutor.course}</h4>

              <div class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 border border-slate-200/80 rounded-xl text-xs text-slate-700 mb-3 w-full">
                <span>🏆 Aprobó con <strong class="text-ucuenca-wine font-extrabold">${tutor.score}</strong> con <span class="italic font-semibold">${tutor.teacher}</span></span>
              </div>

              <div class="flex flex-wrap gap-1.5 mb-4">
                ${tutor.badges.map(b => `<span class="text-[10px] font-semibold text-slate-600 bg-slate-100 px-2 py-0.5 rounded-md">${b}</span>`).join('')}
              </div>
            </div>

            <div class="pt-3.5 border-t border-slate-100 flex items-center justify-between gap-3">
              <div>
                <span class="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">Tarifa</span>
                <span class="text-xl font-black text-ucuenca-navy">$${tutor.hourlyRate.toFixed(2)}</span>
                <span class="text-xs text-slate-500">/h</span>
              </div>
              <button onclick="openBookingModal(${tutor.id})" class="py-2.5 px-4 rounded-xl bg-ucuenca-wine hover:bg-ucuenca-winedark text-white font-bold text-xs shadow-sm flex items-center gap-1">
                <span>Reservar Tutoría</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        `;
      }).join('');
      lucide.createIcons();
    }

    function renderMisSolicitudes() {
      const container = document.getElementById('mis-solicitudes-container');
      document.getElementById('user-req-count').textContent = misSolicitudes.length;
      if (misSolicitudes.length === 0) {
        container.innerHTML = `<p class="text-xs text-slate-400 text-center py-4">No tienes solicitudes activas.</p>`;
        return;
      }
      container.innerHTML = misSolicitudes.map(s => `
        <div class="p-3.5 bg-slate-50 rounded-2xl border border-slate-200 text-xs space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="font-bold text-ucuenca-navy">${s.materia}</span>
            <span class="font-extrabold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">$${s.paga.toFixed(2)}</span>
          </div>
          <p class="text-slate-600 text-[11px]">${s.desc}</p>
          <div class="flex items-center justify-between pt-1 text-[10px] text-slate-400 border-t border-slate-200/60">
            <span>Plazo: ${s.plazo}</span>
            <span class="font-semibold text-ucuenca-wine">👥 ${s.postulantes} tutores listos</span>
          </div>
        </div>
      `).join('');
    }

    function renderCommunity() {
      const container = document.getElementById('community-feed-grid');
      container.innerHTML = communityPosts.map(p => `
        <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-ucuenca-navy">${p.author}</span>
              <span class="px-2 py-0.5 bg-rose-50 text-ucuenca-wine text-[10px] font-bold rounded-md">${p.course}</span>
            </div>
            <p class="text-xs text-slate-700 font-medium mb-3">${p.text}</p>
          </div>
          <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
            <span class="font-extrabold text-emerald-600">Recompensa: $${p.bounty.toFixed(2)}</span>
            <button onclick="showToast('Has postulado para ayudar a ' + '${p.author}', 'success')" class="px-3 py-1.5 rounded-lg bg-ucuenca-navy text-white font-bold text-[11px]">
              Ofrecerme
            </button>
          </div>
        </div>
      `).join('');
      lucide.createIcons();
    }

    function renderBookedClasses() {
      const container = document.getElementById('booked-classes-list');
      document.getElementById('badge-clases-count').textContent = bookedClasses.length;
      if (bookedClasses.length === 0) {
        container.innerHTML = `<div class="bg-white rounded-3xl p-8 text-center text-xs text-slate-400 border">No tienes tutorías activas.</div>`;
        return;
      }
      container.innerHTML = bookedClasses.map(s => `
        <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="flex items-center gap-3.5">
            <img src="${s.avatar}" class="w-12 h-12 rounded-xl object-cover">
            <div>
              <span class="px-2 py-0.5 bg-emerald-50 text-emerald-700 text-[10px] font-bold rounded-md">En Custodia</span>
              <h4 class="text-sm font-bold text-ucuenca-navy mt-0.5">${s.course}</h4>
              <p class="text-xs text-slate-500">Tutor: <strong>${s.tutorName}</strong></p>
            </div>
          </div>
          <div class="text-xs text-slate-600">
            <div>🕒 ${s.date}</div>
            <div>📍 ${s.modality}</div>
          </div>
          <div class="flex items-center gap-2">
            ${s.meetLink ? `
              <a href="${s.meetLink}" target="_blank" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs flex items-center gap-1">
                <i data-lucide="video" class="w-3.5 h-3.5"></i> Abrir Meet
              </a>
            ` : `<span class="text-xs font-mono bg-slate-100 p-2 rounded-lg">QR Presencial</span>`}
            <button onclick="completarClase(${s.id}, ${s.fee})" class="px-3 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs">
              Liberar Pago
            </button>
          </div>
        </div>
      `).join('');
      lucide.createIcons();
    }

    function completarClase(id, fee) {
      bookedClasses = bookedClasses.filter(b => b.id !== id);
      renderBookedClasses();
      showToast(`¡Clase completada! Se transfirieron $${fee.toFixed(2)} al tutor.`, 'success');
    }

    function setActiveTab(tabKey) {
      ['explore', 'request', 'community', 'betutor', 'classes'].forEach(v => {
        const el = document.getElementById(`view-${v}`);
        if (el) el.classList.add('hidden');
      });

      document.querySelectorAll('[id^="nav-btn-"]').forEach(btn => {
        btn.className = "px-3.5 py-2 text-xs font-semibold rounded-xl text-slate-600 hover:text-ucuenca-navy transition-all flex items-center gap-1.5";
      });

      const activeView = document.getElementById(`view-${tabKey}`);
      if (activeView) activeView.classList.remove('hidden');

      const activeBtn = document.getElementById(`nav-btn-${tabKey}`);
      if (activeBtn) {
        if (tabKey === 'request') {
          activeBtn.className = "px-3.5 py-2 text-xs font-bold rounded-xl text-white bg-ucuenca-wine hover:bg-ucuenca-winedark transition-all flex items-center gap-1.5 shadow-sm";
        } else {
          activeBtn.className = "px-3.5 py-2 text-xs font-bold rounded-xl transition-all flex items-center gap-1.5 bg-white text-ucuenca-navy shadow-sm";
        }
      }

      if (tabKey === 'request') renderMisSolicitudes();
      if (tabKey === 'community') renderCommunity();
      if (tabKey === 'classes') renderBookedClasses();

      window.scrollTo({ top: 0, behavior: 'smooth' });
      lucide.createIcons();
    }

    function handleCrearSolicitud(e) {
      e.preventDefault();
      const materia = document.getElementById('req-materia').value;
      const paga = parseFloat(document.getElementById('req-paga').value);
      const plazo = document.getElementById('req-plazo').value;
      const desc = document.getElementById('req-desc').value;

      misSolicitudes.unshift({ id: Date.now(), materia, desc, paga, plazo, postulantes: 0 });
      communityPosts.unshift({ id: Date.now(), author: "Juanita Perez", course: materia, text: desc, bounty: paga });

      e.target.reset();
      renderMisSolicitudes();
      showToast("¡Solicitud publicada en el muro!", "success");
    }

    function handlePostularTutor(e) {
      e.preventDefault();
      const materia = document.getElementById('tutor-reg-materia').value;
      const nota = document.getElementById('tutor-reg-nota').value;
      const docente = document.getElementById('tutor-reg-docente').value;
      const tarifa = parseFloat(document.getElementById('tutor-reg-tarifa').value);
      const mod = document.getElementById('tutor-reg-modalidad').value;

      tutorsData.unshift({
        id: Date.now(),
        name: "Juanita Perez",
        facultyKey: "economicas",
        facultyLabel: "Ciencias Económicas y Adm.",
        course: materia,
        teacher: docente,
        score: nota,
        rating: 5.0,
        reviewsCount: 1,
        hourlyRate: tarifa,
        modality: mod,
        location: mod === 'virtual' ? 'Virtual (Google Meet)' : 'Campus Central',
        avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&h=200&q=80",
        badges: ["Tutor Verificado", "Récord Aprobado"]
      });

      showToast("¡Perfil de tutor publicado exitosamente!", "success");
      setActiveTab('explore');
      renderTutors(tutorsData);
    }

    function handleSearch() {
      const q = document.getElementById('search-input').value.toLowerCase().trim();
      const fac = document.getElementById('faculty-select').value;
      const filtered = tutorsData.filter(t => 
        (fac === 'all' || t.facultyKey === fac) &&
        (t.name.toLowerCase().includes(q) || t.course.toLowerCase().includes(q) || t.teacher.toLowerCase().includes(q))
      );
      renderTutors(filtered);
    }

    function setChipFilter(chip) {
      const filtered = tutorsData.filter(t => chip === 'all' || t.modality === chip);
      renderTutors(filtered);
    }

    function openBookingModal(id) {
      selectedTutor = tutorsData.find(t => t.id === id);
      document.getElementById('modal-tutor-name').textContent = selectedTutor.name;
      document.getElementById('modal-tutor-course').textContent = selectedTutor.course;
      document.getElementById('modal-tutor-avatar').src = selectedTutor.avatar;
      document.getElementById('modal-tutor-merit').textContent = `🏆 Aprobó con ${selectedTutor.score} (${selectedTutor.teacher})`;
      document.getElementById('modal-fee-display').textContent = `$${selectedTutor.hourlyRate.toFixed(2)}`;
      document.getElementById('modal-balance-display').textContent = `$${userBalance.toFixed(2)}`;
      document.getElementById('booking-modal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeBookingModal() {
      document.getElementById('booking-modal').classList.add('hidden');
    }

    function confirmBooking() {
      if (userBalance < selectedTutor.hourlyRate) {
        showToast("Saldo insuficiente. Recarga tu billetera.", "error");
        closeBookingModal();
        openDepositModal();
        return;
      }
      userBalance -= selectedTutor.hourlyRate;
      document.getElementById('user-balance-display').textContent = `$${userBalance.toFixed(2)}`;

      bookedClasses.unshift({
        id: Date.now(),
        tutorName: selectedTutor.name,
        course: selectedTutor.course,
        date: "Mañana, 16:00 - 17:00",
        modality: selectedTutor.location,
        meetLink: selectedTutor.modality === 'virtual' ? 'https://meet.google.com/new' : null,
        fee: selectedTutor.hourlyRate,
        avatar: selectedTutor.avatar
      });

      closeBookingModal();
      showToast(`¡Tutoría confirmada con ${selectedTutor.name}!`, "success");
    }

    function openDepositModal() {
      document.getElementById('deposit-modal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeDepositModal() {
      document.getElementById('deposit-modal').classList.add('hidden');
    }

    function executeDeposit() {
      const val = parseFloat(document.getElementById('deposit-val').value);
      if (val > 0) {
        userBalance += val;
        document.getElementById('user-balance-display').textContent = `$${userBalance.toFixed(2)}`;
        closeDepositModal();
        showToast(`+${val.toFixed(2)} USD acreditados a tu billetera`, "success");
      }
    }

    function showToast(msg, type = 'info') {
      const c = document.getElementById('toast-container');
      const t = document.createElement('div');
      t.className = `p-4 rounded-2xl shadow-xl bg-white border-2 ${type === 'success' ? 'border-emerald-500' : 'border-rose-500'} text-slate-800 text-xs font-bold pointer-events-auto`;
      t.innerHTML = `<span>${msg}</span>`;
      c.appendChild(t);
      setTimeout(() => t.remove(), 3500);
    }

    window.addEventListener('DOMContentLoaded', () => {
      renderTutors(tutorsData);
      renderMisSolicitudes();
      lucide.createIcons();
    });
  </script>
</body>
</html>
"""

# 4. Renderizado en Streamlit
components.html(HTML_APP, height=1350, scrolling=True)