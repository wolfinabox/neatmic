############################################################################################
#      NSIS Installation Script created by NSIS Quick Setup Script Generator v1.09.18
#               Entirely Edited with NullSoft Scriptable Installation System                
#              by Vlasis K. Barkas aka Red Wine red_wine@freemail.gr Sep 2006               
############################################################################################

!define APP_NAME "NeatMic"
!define COMP_NAME "wolfinabox"
!define WEB_SITE "https://github.com/wolfinabox/neatmic"
!define VERSION "00.00.00.01"
!define COPYRIGHT "wolfinabox © 2021"
!define DESCRIPTION "Application"
!define INSTALLER_NAME "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\Output\NeatMic\setup.exe"
!define MAIN_APP_EXE "neatmic.exe"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

######################################################################

VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

######################################################################

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
XPStyle on
InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$PROGRAMFILES\NeatMic"

######################################################################

!include "MUI.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "NeatMic"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

!define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_APP_EXE}"
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

######################################################################

Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\base_library.zip"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\libcrypto-1_1.dll"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\libffi-7.dll"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\libopenblas.XWYDX2IKJW2NMTWSFYNGFUWKQU3LYTCZ.gfortran-win_amd64.dll"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\libssl-1_1.dll"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\neatmic.exe"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\neatmic.exe.manifest"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyexpat.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\python39.dll"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\select.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\unicodedata.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\VCRUNTIME140.dll"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_asyncio.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_bz2.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_cffi_backend.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_ctypes.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_decimal.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_hashlib.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_lzma.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_multiprocessing.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_overlapped.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_queue.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_socket.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_ssl.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\_uuid.pyd"
SetOutPath "$INSTDIR\wheel-0.37.0.dist-info"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\entry_points.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\INSTALLER"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\LICENSE.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\METADATA"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\RECORD"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\top_level.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\wheel-0.37.0.dist-info\WHEEL"
SetOutPath "$INSTDIR\soundcard"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\soundcard\coreaudio.py.h"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\soundcard\mediafoundation.py.h"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\soundcard\pulseaudio.py.h"
SetOutPath "$INSTDIR\setuptools-58.0.4.dist-info"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\entry_points.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\INSTALLER"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\LICENSE"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\METADATA"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\RECORD"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\top_level.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\setuptools-58.0.4.dist-info\WHEEL"
SetOutPath "$INSTDIR\pyinstaller-4.5.1.dist-info"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\COPYING.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\entry_points.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\INSTALLER"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\METADATA"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\RECORD"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\REQUESTED"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\top_level.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\pyinstaller-4.5.1.dist-info\WHEEL"
SetOutPath "$INSTDIR\numpy\random"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\bit_generator.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\mtrand.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_bounded_integers.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_common.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_generator.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_mt19937.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_pcg64.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_philox.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\random\_sfc64.cp39-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\linalg"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\linalg\lapack_lite.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\linalg\_umath_linalg.cp39-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\fft"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\fft\_pocketfft_internal.cp39-win_amd64.pyd"
SetOutPath "$INSTDIR\numpy\core"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\core\_multiarray_tests.cp39-win_amd64.pyd"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\numpy\core\_multiarray_umath.cp39-win_amd64.pyd"
SetOutPath "$INSTDIR\altgraph-0.17.2.dist-info"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\INSTALLER"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\LICENSE"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\METADATA"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\RECORD"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\top_level.txt"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\WHEEL"
File "C:\Users\wolfinabox\Sync\Projects\Python\neatmic\deployment\windows\dist\neatmic\altgraph-0.17.2.dist-info\zip-safe"
SectionEnd

######################################################################

Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\NeatMic"
CreateShortCut "$SMPROGRAMS\NeatMic\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\NeatMic\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\NeatMic\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "Publisher" "${COMP_NAME}"

!ifdef WEB_SITE
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "URLInfoAbout" "${WEB_SITE}"
!endif
SectionEnd

######################################################################

Section Uninstall
${INSTALL_TYPE}
Delete "$INSTDIR\base_library.zip"
Delete "$INSTDIR\libcrypto-1_1.dll"
Delete "$INSTDIR\libffi-7.dll"
Delete "$INSTDIR\libopenblas.XWYDX2IKJW2NMTWSFYNGFUWKQU3LYTCZ.gfortran-win_amd64.dll"
Delete "$INSTDIR\libssl-1_1.dll"
Delete "$INSTDIR\neatmic.exe"
Delete "$INSTDIR\neatmic.exe.manifest"
Delete "$INSTDIR\pyexpat.pyd"
Delete "$INSTDIR\python39.dll"
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\VCRUNTIME140.dll"
Delete "$INSTDIR\_asyncio.pyd"
Delete "$INSTDIR\_bz2.pyd"
Delete "$INSTDIR\_cffi_backend.cp39-win_amd64.pyd"
Delete "$INSTDIR\_ctypes.pyd"
Delete "$INSTDIR\_decimal.pyd"
Delete "$INSTDIR\_hashlib.pyd"
Delete "$INSTDIR\_lzma.pyd"
Delete "$INSTDIR\_multiprocessing.pyd"
Delete "$INSTDIR\_overlapped.pyd"
Delete "$INSTDIR\_queue.pyd"
Delete "$INSTDIR\_socket.pyd"
Delete "$INSTDIR\_ssl.pyd"
Delete "$INSTDIR\_uuid.pyd"
Delete "$INSTDIR\wheel-0.37.0.dist-info\entry_points.txt"
Delete "$INSTDIR\wheel-0.37.0.dist-info\INSTALLER"
Delete "$INSTDIR\wheel-0.37.0.dist-info\LICENSE.txt"
Delete "$INSTDIR\wheel-0.37.0.dist-info\METADATA"
Delete "$INSTDIR\wheel-0.37.0.dist-info\RECORD"
Delete "$INSTDIR\wheel-0.37.0.dist-info\top_level.txt"
Delete "$INSTDIR\wheel-0.37.0.dist-info\WHEEL"
Delete "$INSTDIR\soundcard\coreaudio.py.h"
Delete "$INSTDIR\soundcard\mediafoundation.py.h"
Delete "$INSTDIR\soundcard\pulseaudio.py.h"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\entry_points.txt"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\INSTALLER"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\LICENSE"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\METADATA"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\RECORD"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\top_level.txt"
Delete "$INSTDIR\setuptools-58.0.4.dist-info\WHEEL"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\COPYING.txt"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\entry_points.txt"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\INSTALLER"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\METADATA"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\RECORD"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\REQUESTED"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\top_level.txt"
Delete "$INSTDIR\pyinstaller-4.5.1.dist-info\WHEEL"
Delete "$INSTDIR\numpy\random\bit_generator.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\mtrand.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_bounded_integers.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_common.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_generator.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_mt19937.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_pcg64.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_philox.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\random\_sfc64.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\linalg\lapack_lite.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\linalg\_umath_linalg.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\fft\_pocketfft_internal.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\core\_multiarray_tests.cp39-win_amd64.pyd"
Delete "$INSTDIR\numpy\core\_multiarray_umath.cp39-win_amd64.pyd"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\INSTALLER"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\LICENSE"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\METADATA"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\RECORD"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\top_level.txt"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\WHEEL"
Delete "$INSTDIR\altgraph-0.17.2.dist-info\zip-safe"
 
RmDir "$INSTDIR\altgraph-0.17.2.dist-info"
RmDir "$INSTDIR\numpy\core"
RmDir "$INSTDIR\numpy\fft"
RmDir "$INSTDIR\numpy\linalg"
RmDir "$INSTDIR\numpy\random"
RmDir "$INSTDIR\pyinstaller-4.5.1.dist-info"
RmDir "$INSTDIR\setuptools-58.0.4.dist-info"
RmDir "$INSTDIR\soundcard"
RmDir "$INSTDIR\wheel-0.37.0.dist-info"
 
Delete "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
Delete "$INSTDIR\${APP_NAME} website.url"
!endif

RmDir "$INSTDIR"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\NeatMic\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\NeatMic\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\NeatMic\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\NeatMic"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd

######################################################################

