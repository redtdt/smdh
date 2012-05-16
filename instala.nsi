SetCompressor /SOLID LZMA
; example1.nsi
;
; This script is perhaps one of the simplest NSIs you can make. All of the
; optional settings are left to their default settings. The installer simply 
; prompts the user asking them where to install, and drops a copy of example1.nsi
; there. 

;--------------------------------

; The name of the installer
Name "SMDH"

; The file to write
OutFile "instala.exe"

; The default installation directory
InstallDir c:\smdh2

; Request application privileges for Windows Vista
RequestExecutionLevel user
LicenseText "Licencia"
LicenseData "licencia.txt"
;--------------------------------

; Pages
Page license
Page directory
Page instfiles

;--------------------------------

; The stuff to install
Section "Install" ;No components page, name is not important

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  File /r dist\*
  SetShellVarContext all
  ;CreateShortCut $SMPROGRAMS\$R0\smdh.lnk $INSTDIR\bin\smdh.exe
  CreateShortCut $SMPROGRAMS\smdh.lnk $INSTDIR\bin\smdh.exe

  
SectionEnd ; end the section


