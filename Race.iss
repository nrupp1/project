; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Race"
#define MyAppVersion "1.5"
#define MyAppPublisher "CushionyInk5575"
#define MyAppExeName "Race.exe"
#define MyAppAssocName MyAppName + ""
#define MyAppAssocExt ".exe"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
AppId={{9E10A231-1410-4C72-8C2F-9595E81060C8}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={userdesktop}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
OutputBaseFilename=mysetup
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Add necessary Python DLLs
Source: "C:\Users\natha\AppData\Local\Programs\Python\Python312\DLLs\sqlite3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\AppData\Local\Programs\Python\Python312\DLLs\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\AppData\Local\Programs\Python\Python312\DLLs\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\python312.dll"; DestDir: "{app}"; Flags: ignoreversion

; Include the required DLLs from the pygame directory
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\zlib1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\portmidi.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libwebp-7.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libtiff-5.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libpng16-16.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libopusfile-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libopus-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libogg-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libmodplug-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\libjpeg-9.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\freetype.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\SDL2_ttf.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\SDL2_mixer.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\SDL2_image.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\pygame\SDL2.dll"; DestDir: "{app}"; Flags: ignoreversion

; Include the required DLLs from the lib directory
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\libcrypto-3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\libffi-8.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\lib\libssl-3.dll"; DestDir: "{app}"; Flags: ignoreversion

; Add other necessary game assets
Source: "C:\Users\natha\PycharmProjects\setup\build\exe.win-amd64-3.12\Race.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\pythonProject\road.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\pythonProject\car1.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\natha\PycharmProjects\pythonProject\car2.png"; DestDir: "{app}"; Flags: ignoreversion
; Add all other assets as needed

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon