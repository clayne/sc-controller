"""
hidparse_data - long enums moved from hidparse.py

Licensed under GPL 2.0
"""

from scc.lib import IntEnum


class MainItem(IntEnum):
	Input = 0x80
	Output = 0x90
	Collection = 0xA0
	Feature = 0xB0
	EndCollection = 0xC0


class GlobalItem(IntEnum):
	UsagePage = 0x00
	LogicalMinimum = 0x10
	LogicalMaximum = 0x20
	PhysicalMinimum = 0x30
	PhysicalMaximum = 0x40
	UnitExponent = 0x50
	Unit = 0x60
	ReportSize = 0x70
	ReportID = 0x80
	ReportCount = 0x90
	Push = 0xA0
	Pop = 0xB0


class LocalItem(IntEnum):
	Usage = 0x00
	UsageMinimum = 0x10
	UsageMaximum = 0x20
	DesignatorIndex = 0x30
	DesignatorMinimum = 0x40
	DesignatorMaximum = 0x50
	StringIndex = 0x70
	StringMinimum = 0x80
	StringMaximum = 0x90
	Delimiter = 0xA0


class Collection(IntEnum):
	Physical = 0x00
	Application = 0x01
	Logical = 0x02
	Report = 0x03
	NamedArray = 0x04
	UsageSwitch = 0x05
	UsageModifier = 0x06


class GenericDesktopPage(IntEnum):
	Undefined = 0x00
	Pointer = 0x01
	Mouse = 0x02
	Reserved = 0x03
	Joystick = 0x04
	GamePad = 0x05
	Keyboard = 0x06
	Keypad = 0x07
	MultiAxisController = 0x08
	TabletPCSystemControls = 0x09
	X = 0x30
	Y = 0x31
	Z = 0x32
	Rx = 0x33
	Ry = 0x34
	Rz = 0x35
	Slider = 0x36
	Dial = 0x37
	Wheel = 0x38
	Hatswitch = 0x39
	CountedBuffer = 0x3A
	ByteCount = 0x3B
	MotionWakeup = 0x3C
	Start = 0x3D
	Select = 0x3E
	Vx = 0x40
	Vy = 0x41
	Vz = 0x42
	Vbrx = 0x43
	Vbry = 0x44
	Vbrz = 0x45
	Vno = 0x46
	FeatureNotification = 0x47
	ResolutionMultiplier = 0x48
	SystemControl = 0x80
	SystemPowerDown = 0x81
	SystemSleep = 0x82
	SystemWakeUp = 0x83
	SystemContextMenu = 0x84
	SystemMainMenu = 0x85
	SystemAppMenu = 0x86
	SystemMenuHelp = 0x87
	SystemMenuExit = 0x88
	SystemMenuSelect = 0x89
	SystemMenuRight = 0x8A
	SystemMenuLeft = 0x8B
	SystemMenuUp = 0x8C
	SystemMenuDown = 0x8D
	SystemColdRestart = 0x8E
	SystemWarmRestart = 0x8F
	DPadUp = 0x90
	DPadDown = 0x91
	DPadRight = 0x92
	DPadLeft = 0x93
	SystemDock = 0xA0
	SystemUndock = 0xA1
	SystemSetup = 0xA2
	SystemBreak = 0xA3
	SystemDebuggerBreak = 0xA4
	ApplicationBreak = 0xA5
	ApplicationDebuggerBreak = 0xA6
	SystemSpeakerMute = 0xA7
	SystemHibernate = 0xA8
	SystemDisplayInvert = 0xB0
	SystemDisplayInternal = 0xB1
	SystemDisplayExternal = 0xB2
	SystemDisplayBoth = 0xB3
	SystemDisplayDual = 0xB4
	SystemDisplayToggleIntExt = 0xB5
	SystemDisplaySwapPrimarySecondary = 0xB6
	SystemDisplayLCDAutoscale = 0xB7


class SimulationControlsPage(IntEnum):
	Undefined = 0x00
	FlightSimulationDevice = 0x01
	AutomobileSimulationDevice = 0x02
	TankSimulationDevice = 0x03
	SpaceshipSimulationDevice = 0x04
	SubmarineSimulationDevice = 0x05
	SailingSimulationDevice = 0x06
	MotorcycleSimulationDevice = 0x07
	SportsSimulationDevice = 0x08
	AirplaneSimulationDevice = 0x09
	HelicopterSimulationDevice = 0x0A
	MagicCarpetSimulationDevice = 0x0B
	BicycleSimulationDevice = 0x0C
	FlightControlStick = 0x20
	FlightStick = 0x21
	CyclicControl = 0x22
	CyclicTrim = 0x23
	FlightYoke = 0x24
	TrackControl = 0x25
	Aileron = 0xB0
	AileronTrim = 0xB1
	AntiTorqueControl = 0xB2
	AutopilotEnable = 0xB3
	ChaffRelease = 0xB4
	CollectiveControl = 0xB5
	DiveBrake = 0xB6
	ElectronicCountermeasures = 0xB7
	Elevator = 0xB8
	ElevatorTrim = 0xB9
	Rudder = 0xBA
	Throttle = 0xBB
	FlightCommunications = 0xBC
	FlareRelease = 0xBD
	LandingGear = 0xBE
	ToeBrake = 0xBF
	Trigger = 0xC0
	WeaponsArm = 0xC1
	WeaponsSelect = 0xC2
	WingFlaps = 0xC3
	Accelerator = 0xC4
	Brake = 0xC5
	Clutch = 0xC6
	Shifter = 0xC7
	Steering = 0xC8
	TurretDirection = 0xC9
	BarrelElevation = 0xCA
	DivePlane = 0xCB
	Ballast = 0xCC
	BicycleCrank = 0xCD
	HandleBars = 0xCE
	FrontBrake = 0xCF
	RearBrake = 0xD0


class VRControlsPage(IntEnum):
	Unidentified = 0x00
	Belt = 0x01
	BodySuit = 0x02
	Flexor = 0x03
	Glove = 0x04
	HeadTracker = 0x05
	HeadMountedDisplay = 0x06
	HandTracker = 0x07
	Oculometer = 0x08
	Vest = 0x09
	AnimatronicDevice = 0x0A
	StereoEnable = 0x20
	DisplayEnable = 0x21


class SportControlsPage(IntEnum):
	Unidentified = 0x00
	BaseballBat = 0x01
	GolfClub = 0x02
	RowingMachine = 0x03
	Treadmill = 0x04
	Oar = 0x30
	Slope = 0x31
	Rate = 0x32
	StickSpeed = 0x33
	StickFaceAngle = 0x34
	StickHeelToe = 0x35
	StickFollowThrough = 0x36
	StickTempo = 0x37
	StickType = 0x38
	StickHeight = 0x39
	Putter = 0x50
	Iron1 = 0x51
	Iron2 = 0x52
	Iron3 = 0x53
	Iron4 = 0x54
	Iron5 = 0x55
	Iron6 = 0x56
	Iron7 = 0x57
	Iron8 = 0x58
	Iron9 = 0x59
	Iron10 = 0x5A
	Iron11 = 0x5B
	SandWedge = 0x5C
	LoftWedge = 0x5D
	PowerWedge = 0x5E
	Wood1 = 0x5F
	Wood3 = 0x60
	Wood5 = 0x61
	Wood7 = 0x62
	Wood9 = 0x63


class GameControlsPage(IntEnum):
	Undefined = 0x00
	GameController3D = 0x01
	PinballDevice = 0x02
	GunDevice = 0x03
	PointofView = 0x20
	TurnRightLeft = 0x21
	PitchForwardBackward = 0x22
	RollRightLeft = 0x23
	MoveRightLeft = 0x24
	MoveForwardBackward = 0x25
	MoveUpDown = 0x26
	LeanRightLeft = 0x27
	LeanForwardBackward = 0x28
	HeightofPOV = 0x29
	Flipper = 0x2A
	SecondaryFlipper = 0x2B
	Bump = 0x2C
	NewGame = 0x2D
	ShootBall = 0x2E
	Player = 0x2F
	GunBolt = 0x30
	GunClip = 0x31
	GunSelector = 0x32
	GunSingleShot = 0x33
	GunBurst = 0x34
	GunAutomatic = 0x35
	GunSafety = 0x36
	GamepadFireJump = 0x37
	GamepadTrigger = 0x39


class GenericDeviceControlsPage(IntEnum):
	Unidentified = 0x00
	BatteryStrength = 0x20
	WirelessChannel = 0x21
	WirelessID = 0x22
	DiscoverWirelessControl = 0x23
	SecurityCodeCharacterEntered = 0x24
	SecurityCodeCharacterErased = 0x25
	SecurityCodeCleared = 0x26


class KeyboardKeypadPage(IntEnum):
	NoEventIndicated = 0x00
	ErrorRollOver = 0x01
	POSTFail = 0x02
	ErrorUndefined = 0x03
	A = 0x04
	B = 0x05
	C = 0x06
	D = 0x07
	E = 0x08
	F = 0x09
	G = 0x0A
	H = 0x0B
	I = 0x0C
	J = 0x0D
	K = 0x0E
	L = 0x0F
	M = 0x10
	N = 0x11
	O = 0x12
	P = 0x13
	Q = 0x14
	R = 0x15
	S = 0x16
	T = 0x17
	U = 0x18
	V = 0x19
	W = 0x1A
	X = 0x1B
	Y = 0x1C
	Z = 0x1D
	Num1 = 0x1E
	Num2 = 0x1F
	Num3 = 0x20
	Num4 = 0x21
	Num5 = 0x22
	Num6 = 0x23
	Num7 = 0x24
	Num8 = 0x25
	Num9 = 0x26
	Num0 = 0x27
	Enter = 0x28
	Escape = 0x29
	Delete = 0x2A
	Tab = 0x2B
	Spacebar = 0x2C
	Minus = 0x2D
	Plus = 0x2E
	LBrace = 0x2F
	RBrace = 0x30
	Backslash = 0x31
	NonUsGrave = 0x32
	Colon = 0x33
	Doublequote = 0x34
	Grave = 0x35
	Comma = 0x36
	Dot = 0x37
	Slash = 0x38
	CapsLock = 0x39
	F1 = 0x3A
	F2 = 0x3B
	F3 = 0x3C
	F4 = 0x3D
	F5 = 0x3E
	F6 = 0x3F
	F7 = 0x40
	F8 = 0x41
	F9 = 0x42
	F10 = 0x43
	F11 = 0x44
	F12 = 0x45
	PrintScreen = 0x46
	ScrollLock = 0x47
	Pause = 0x48
	Insert = 0x49
	Home = 0x4A
	PageUp = 0x4B
	DeleteForward = 0x4C
	End = 0x4D
	PageDown = 0x4E
	RightArrow = 0x4F
	LeftArrow = 0x50
	DownArrow = 0x51
	UpArrow = 0x52
	NumpadLockandClear = 0x53
	NumpadDivide = 0x54
	NumpadMultiply = 0x55
	NumpadMinus = 0x56
	NumpadPlus = 0x57
	NumpadEnter = 0x58
	Numpad1 = 0x59
	Numpad2 = 0x5A
	Numpad3 = 0x5B
	Numpad4 = 0x5C
	Numpad5 = 0x5D
	Numpad6 = 0x5E
	Numpad7 = 0x5F
	Numpad8 = 0x60
	Numpad9 = 0x61
	Numpad0 = 0x62
	NumpadDot = 0x63
	NonUSBackslash = 0x64
	Application = 0x65
	Power = 0x66
	Equals = 0x67
	F13 = 0x68
	F14 = 0x69
	F15 = 0x6A
	F16 = 0x6B
	F17 = 0x6C
	F18 = 0x6D
	F19 = 0x6E
	F20 = 0x6F
	F21 = 0x70
	F22 = 0x71
	F23 = 0x72
	F24 = 0x73
	Execute = 0x74
	Help = 0x75
	Menu = 0x76
	Select = 0x77
	Stop = 0x78
	Again = 0x79
	Undo = 0x7A
	Cut = 0x7B
	Copy = 0x7C
	Paste = 0x7D
	Find = 0x7E
	Mute = 0x7F
	VolumeUp = 0x80
	VolumeDown = 0x81
	LockingCapsLock = 0x82
	LockingNumLock = 0x83
	LockingScrollLock = 0x84
	CommaSign = 0x85
	EqualSign = 0x86
	KeyboardInternational = 0x87
	# KeyboardInternational = 0x88
	# KeyboardInternational = 0x89
	# KeyboardInternational = 0x8A
	# KeyboardInternational = 0x8B
	# KeyboardInternational = 0x8C
	# KeyboardInternational = 0x8D
	# KeyboardInternational = 0x8E
	# KeyboardInternational = 0x8F
	KeyboardLANG1 = 0x90
	KeyboardLANG2 = 0x91
	KeyboardLANG3 = 0x92
	KeyboardLANG4 = 0x93
	KeyboardLANG5 = 0x94
	KeyboardLANG6 = 0x95
	KeyboardLANG7 = 0x96
	KeyboardLANG8 = 0x97
	KeyboardLANG9 = 0x98
	KeyboardAlternateErase = 0x99
	KeyboardSysReqAttention = 0x9A
	KeyboardCancel = 0x9B
	KeyboardClear = 0x9C
	KeyboardPrior = 0x9D
	KeyboardReturn = 0x9E
	KeyboardSeparator = 0x9F
	KeyboardOut = 0xA0
	KeyboardOper = 0xA1
	KeyboardClearAgain = 0xA2
	KeyboardCrSelProps = 0xA3
	KeyboardExSel = 0xA4
	Keypad00 = 0xB0
	Keypad000 = 0xB1
	ThousandsSeparator = 0xB2
	DecimalSeparator = 0xB3
	CurrencyUnit = 0xB4
	CurrencySubUnit34 = 0xB5
	KeypadLeftBracket = 0xB6
	KeypadRightBracket = 0xB7
	KeypadLeftBrace = 0xB8
	KeypadRightBrace = 0xB9
	# Tab = 0xBA
	Backspace = 0xBB
	# A = 0xBC
	# B = 0xBD
	# C = 0xBE
	# D = 0xBF
	# E = 0xC0
	# F = 0xC1
	Xox = 0xC2
	KeyXor = 0xC3
	KeyPercent = 0xC4
	KeyLessThan = 0xC5
	KeyMoreThan = 0xC6
	KeyAnd = 0xC7
	KeyAndAnd = 0xC8
	KeyOr = 0xC9
	KeyOrOr = 0xCA
	KeyColon = 0xCB
	KeyHash = 0xCC
	Space = 0xCD
	KeyAt = 0xCE
	KeyExclamation = 0xCF
	MemoryStore = 0xD0
	MemoryRecall = 0xD1
	MemoryClear = 0xD2
	MemoryAdd = 0xD3
	MemorySubtract = 0xD4
	MemoryMultiply = 0xD5
	MemoryDivide = 0xD6
	PlusMinus = 0xD7
	Clear = 0xD8
	ClearEntry = 0xD9
	Binary = 0xDA
	Octal = 0xDB
	Decimal = 0xDC
	KeypadHexadecimal = 0xDD
	KeyboardLeftControl = 0xE0
	KeyboardLeftShift = 0xE1
	KeyboardLeftAlt = 0xE2
	KeyboardLeftGUI = 0xE3
	KeyboardRightControl = 0xE4
	KeyboardRightShift = 0xE5
	KeyboardRightAlt = 0xE6
	KeyboardRightGUI = 0xE7


class LedPage(IntEnum):
	Undefined = 0x00
	NumLock = 0x01
	CapsLock = 0x02
	ScrollLock = 0x03
	Compose = 0x04
	Kana = 0x05
	Power = 0x06
	Shift = 0x07
	DoNotDisturb = 0x08
	Mute = 0x09
	ToneEnable = 0x0A
	HighCutFilter = 0x0B
	LowCutFilter = 0x0C
	EqualizerEnable = 0x0D
	SoundFieldOn = 0x0E
	SurroundOn = 0x0F
	Repeat = 0x10
	Stereo = 0x11
	SamplingRateDetect = 0x12
	Spinning = 0x13
	CAV = 0x14
	CLV = 0x15
	RecordingFormatDetect = 0x16
	OffHook = 0x17
	Ring = 0x18
	MessageWaiting = 0x19
	DataMode = 0x1A
	BatteryOperation = 0x1B
	BatteryOK = 0x1C
	BatteryLow = 0x1D
	Speaker = 0x1E
	HeadSet = 0x1F
	Hold = 0x20
	Microphone = 0x21
	Coverage = 0x22
	NightMode = 0x23
	SendCalls = 0x24
	CallPickup = 0x25
	Conference = 0x26
	StandBy = 0x27
	CameraOn = 0x28
	CameraOff = 0x29
	OnLine = 0x2A
	OffLine = 0x2B
	Busy = 0x2C
	Ready = 0x2D
	PaperOut = 0x2E
	PaperJam = 0x2F
	Remote = 0x30
	Forward = 0x31
	Reverse = 0x32
	Stop = 0x33
	Rewind = 0x34
	FastForward = 0x35
	Play = 0x36
	Pause = 0x37
	Record = 0x38
	Error = 0x39
	UsageSelectedIndicator = 0x3A
	UsageInUseIndicator = 0x3B
	UsageMultiModeIndicator = 0x3C
	IndicatorOn = 0x3D
	IndicatorFlash = 0x3E
	IndicatorSlowBlink = 0x3F
	IndicatorFastBlink = 0x40
	IndicatorOff = 0x41
	FlashOnTime = 0x42
	SlowBlinkOnTime = 0x43
	SlowBlinkOffTime = 0x44
	FastBlinkOnTime = 0x45
	FastBlinkOffTime = 0x46
	UsageIndicatorColor = 0x47
	IndicatorRed = 0x48
	IndicatorGreen = 0x49
	IndicatorAmber = 0x4A
	GenericIndicator = 0x4B
	SystemSuspend = 0x4C
	ExternalPowerConnected = 0x4D


class ButtonPage(IntEnum):
	NoButtonPressed = 0x00
	Button1 = 0x01
	Button2 = 0x02
	Button3 = 0x03
	Button4 = 0x04


class OrdinalPage(IntEnum):
	Instance1 = 0x01
	Instance2 = 0x02
	Instance3 = 0x03
	Instance4 = 0x04


class TelephonyDevicePage(IntEnum):
	Unassigned = 0x00
	Phone = 0x01
	AnsweringMachine = 0x02
	MessageControls = 0x03
	Handset = 0x04
	Headset = 0x05
	TelephonyKeyPad = 0x06
	ProgrammableButton = 0x07
	HookSwitch = 0x20
	Flash = 0x21
	Feature = 0x22
	Hold = 0x23
	Redial = 0x24
	Transfer = 0x25
	Drop = 0x26
	Park = 0x27
	ForwardCalls = 0x28
	AlternateFunction = 0x29
	Line = 0x2A
	SpeakerPhone = 0x2B
	Conference = 0x2C
	RingEnable = 0x2D
	RingSelect = 0x2E
	PhoneMute = 0x2F
	CallerID = 0x30
	Send = 0x31
	SpeedDial = 0x50
	StoreNumber = 0x51
	RecallNumber = 0x52
	PhoneDirectory = 0x53
	VoiceMail = 0x70
	ScreenCalls = 0x71
	DoNotDisturb = 0x72
	Message = 0x73
	AnswerOnOff = 0x74
	InsideDialTone = 0x90
	OutsideDialTone = 0x91
	InsideRingTone = 0x92
	OutsideRingTone = 0x93
	PriorityRingTone = 0x94
	InsideRingback = 0x95
	PriorityRingback = 0x96
	LineBusyTone = 0x97
	ReorderTone = 0x98
	CallWaitingTone = 0x99
	ConfirmationTone1 = 0x9A
	ConfirmationTone2 = 0x9B
	TonesOff = 0x9C
	OutsideRingback = 0x9D
	Ringer = 0x9E
	PhoneKey0 = 0xB0
	PhoneKey1 = 0xB1
	PhoneKey2 = 0xB2
	PhoneKey3 = 0xB3
	PhoneKey4 = 0xB4
	PhoneKey5 = 0xB5
	PhoneKey6 = 0xB6
	PhoneKey7 = 0xB7
	PhoneKey8 = 0xB8
	PhoneKey9 = 0xB9
	PhoneKeyStar = 0xBA
	PhoneKeyPound = 0xBB
	PhoneKeyA = 0xBC
	PhoneKeyB = 0xBD
	PhoneKeyC = 0xBE
	PhoneKeyD = 0xBF


class ConsumerPage(IntEnum):
	Unassigned = 0x00
	ConsumerControl = 0x01
	NumericKeyPad = 0x02
	ProgrammableButtons = 0x03
	Microphone = 0x04
	Headphone = 0x05
	GraphicEqualizer = 0x06
	Plus10 = 0x20
	Plus100 = 0x21
	AMPM = 0x22
	Power = 0x30
	Reset = 0x31
	Sleep = 0x32
	SleepAfter = 0x33
	SleepMode = 0x34
	Illumination = 0x35
	FunctionButtons = 0x36
	Menu = 0x40
	MenuPick = 0x41
	MenuUp = 0x42
	MenuDown = 0x43
	MenuLeft = 0x44
	MenuRight = 0x45
	MenuEscape = 0x46
	MenuValueIncrease = 0x47
	MenuValueDecrease = 0x48
	DataOnScreen = 0x60
	ClosedCaption = 0x61
	ClosedCaptionSelect = 0x62
	VCRTV = 0x63
	BroadcastMode = 0x64
	Snapshot = 0x65
	Still = 0x66
	Selection = 0x80
	AssignSelection = 0x81
	ModeStep = 0x82
	RecallLast = 0x83
	EnterChannel = 0x84
	OrderMovie = 0x85
	Channel = 0x86
	MediaSelection = 0x87
	MediaSelectComputer = 0x88
	MediaSelectTV = 0x89
	MediaSelectWWW = 0x8A
	MediaSelectDVD = 0x8B
	MediaSelectTelephone = 0x8C
	MediaSelectProgramGuide = 0x8D
	MediaSelectVideoPhone = 0x8E
	MediaSelectGames = 0x8F
	MediaSelectMessages = 0x90
	MediaSelectCD = 0x91
	MediaSelectVCR = 0x92
	MediaSelectTuner = 0x93
	Quit = 0x94
	Help = 0x95
	MediaSelectTape = 0x96
	MediaSelectCable = 0x97
	MediaSelectSatellite = 0x98
	MediaSelectSecurity = 0x99
	MediaSelectHome = 0x9A
	MediaSelectCall = 0x9B
	ChannelIncrement = 0x9C
	ChannelDecrement = 0x9D
	MediaSelectSAP = 0x9E
	VCRPlus = 0xA0
	Once = 0xA1
	Daily = 0xA2
	Weekly = 0xA3
	Monthly = 0xA4
	Play = 0xB0
	Pause = 0xB1
	Record = 0xB2
	FastForward = 0xB3
	Rewind = 0xB4
	ScanNextTrack = 0xB5
	ScanPreviousTrack = 0xB6
	Stop = 0xB7
	Eject = 0xB8
	RandomPlay = 0xB9
	SelectDisc = 0xBA
	EnterDisc = 0xBB
	Repeat = 0xBC
	Tracking = 0xBD
	TrackNormal = 0xBE
	SlowTracking = 0xBF
	FrameForward = 0xC0
	FrameBack = 0xC1
	Mark = 0xC2
	ClearMark = 0xC3
	RepeatFromMark = 0xC4
	ReturnToMark = 0xC5
	SearchMarkForward = 0xC6
	SearchMarkBackwards = 0xC7
	CounterReset = 0xC8
	ShowCounter = 0xC9
	TrackingIncrement = 0xCA
	TrackingDecrement = 0xCB
	StopEject = 0xCC
	PlayPause = 0xCD
	PlaySkip = 0xCE
	Volume = 0xE0
	Balance = 0xE1
	Mute = 0xE2
	Bass = 0xE3
	Treble = 0xE4
	BassBoost = 0xE5
	SurroundMode = 0xE6
	Loudness = 0xE7
	MPX = 0xE8
	VolumeIncrement = 0xE9
	VolumeDecrement = 0xEA
	SpeedSelect = 0xF0
	PlaybackSpeed = 0xF1
	StandardPlay = 0xF2
	LongPlay = 0xF3
	ExtendedPlay = 0xF4
	Slow = 0xF5
	FanEnable = 0x100
	FanSpeed = 0x101
	LightEnable = 0x102
	LightIlluminationLevel = 0x103
	ClimateControlEnable = 0x104
	RoomTemperature = 0x105
	SecurityEnable = 0x106
	FireAlarm = 0x107
	PoliceAlarm = 0x108
	Proximity = 0x109
	Motion = 0x10A
	DuressAlarm = 0x10B
	HoldupAlarm = 0x10C
	MedicalAlarm = 0x10D
	BalanceRight = 0x150
	BalanceLeft = 0x151
	BassIncrement = 0x152
	BassDecrement = 0x153
	TrebleIncrement = 0x154
	TrebleDecrement = 0x155
	SpeakerSystem = 0x160
	ChannelLeft = 0x161


class DigitizersPage(IntEnum):
	Undefined = 0x00
	Digitizer = 0x01
	Pen = 0x02
	LightPen = 0x03
	TouchScreen = 0x04
	TouchPad = 0x05
	WhiteBoard = 0x06
	CoordinateMeasuringMachine = 0x07
	Digitizer3D = 0x08
	StereoPlotter = 0x09
	ArticulatedArm = 0x0A
	Armature = 0x0B
	MultiplePointDigitizer = 0x0C
	FreeSpaceWand = 0x0D
	Stylus = 0x20
	Puck = 0x21
	Finger = 0x22
	TipPressure = 0x30
	BarrelPressure = 0x31
	InRange = 0x32
	Touch = 0x33
	Untouch = 0x34
	Tap = 0x35
	Quality = 0x36
	DataValid = 0x37
	TransducerIndex = 0x38
	TabletFunctionKeys = 0x39
	ProgramChangeKeys = 0x3A
	BatteryStrength = 0x3B
	Invert = 0x3C
	XTilt = 0x3D
	YTilt = 0x3E
	Azimuth = 0x3F
	Altitude = 0x40
	Twist = 0x41
	TipSwitch = 0x42
	SecondaryTipSwitch = 0x43
	BarrelSwitch = 0x44
	Eraser = 0x45
	TabletPick = 0x46


class AlphanumericDisplayPage(IntEnum):
	Undefined = 0x00
	AlphanumericDisplay = 0x01
	BitmappedDisplay = 0x02
	DisplayAttributesReport = 0x20
	ASCIICharacterSet = 0x21
	DataReadBack = 0x22
	FontReadBack = 0x23
	DisplayControlReport = 0x24
	ClearDisplay = 0x25
	DisplayEnable = 0x26
	ScreenSaverDelay = 0x27
	ScreenSaverEnable = 0x28
	VerticalScroll = 0x29
	HorizontalScroll = 0x2A
	CharacterReport = 0x2B
	DisplayData = 0x2C
	DisplayStatus = 0x2D
	StatNotReady = 0x2E
	StatReady = 0x2F
	ErrNotaloadablecharacter = 0x30
	ErrFontdatacannotberead = 0x31
	CursorPositionReport = 0x32
	Row = 0x33
	Column = 0x34
	Rows = 0x35
	Columns = 0x36
	CursorPixelPositioning = 0x37
	CursorMode = 0x38
	CursorEnable = 0x39
	CursorBlink = 0x3A
	FontReport = 0x3B
	FontData = 0x3C
	CharacterWidth = 0x3D
	CharacterHeight = 0x3E
	CharacterSpacingHorizontal = 0x3F
	CharacterSpacingVertical = 0x40
	UnicodeCharacterSet = 0x41
	Font7Segment = 0x42
	DirectMap7Segment = 0x43
	Font14Segment = 0x44
	DirectMap14Segment = 0x45
	DisplayBrightness = 0x46
	DisplayContrast = 0x47
	CharacterAttribute = 0x48
	AttributeReadback = 0x49
	AttributeData = 0x4A
	CharAttrEnhance = 0x4B
	CharAttrUnderline = 0x4C
	CharAttrBlink = 0x4D
	BitmapSizeX = 0x80
	BitmapSizeY = 0x81
	BitDepthFormat = 0x83
	DisplayOrientation = 0x84
	PaletteReport = 0x85
	PaletteDataSize = 0x86
	PaletteDataOffset = 0x87
	PaletteData = 0x88
	BlitReport = 0x8A
	BlitRectangleX1 = 0x8B
	BlitRectangleY1 = 0x8C
	BlitRectangleX2 = 0x8D
	BlitRectangleY2 = 0x8E
	BlitData = 0x8F
	SoftButton = 0x90
	SoftButtonID = 0x91
	SoftButtonSide = 0x92
	SoftButtonOffset1 = 0x93
	SoftButtonOffset2 = 0x94
	SoftButtonReport = 0x95


class SensorPage(IntEnum):
	SensorTypeCollection = 0x01
	BiometricHumanPresence = 0x11
	BiometricHumanProximity = 0x12
	BiometricHumanTouch = 0x13
	ElectricalCurrent = 0x22
	ElectricalPower = 0x23
	ElectricalVoltage = 0x26
	ElectricalPotentiometer = 0x27
	ElectricalFrequency = 0x28
	EnvironmentalAtmosphericPressure = 0x31
	EnvironmentalHumidity = 0x32
	EnvironmentalTemperature = 0x33
	LightAmbientLight = 0x41
	MechanicalBooleanSwitch = 0x61
	MechanicalBooleanSwitchArray = 0x62
	MechanicalMultivalueSwitch = 0x63
	MotionAccelerometer1D = 0x71
	MotionAccelerometer2D = 0x72
	MotionAccelerometer3D = 0x73
	MotionGyrometer1D = 0x74
	MotionGyrometer2D = 0x75
	MotionGyrometer3D = 0x76
	MotionMotionDetector = 0x77
	OrientationCompass1D = 0x81
	OrientationCompass3D = 0x83
	OrientationInclinometer1D = 0x84
	OrientationInclinometer2D = 0x85
	OrientationInclinometer3D = 0x86
	OrientationDistance1D = 0x87
	OrientationDistance2D = 0x88
	OrientationDistance3D = 0x89
	OrientationDeviceOrientation = 0x8A
	OtherCustom = 0xE1
	OtherGeneric = 0xE2


class MedicalInstrumentPage(IntEnum):
	Undefined = 0x00
	MedicalUltrasound = 0x01
	VCRAcquisition = 0x20
	FreezeThaw = 0x21
	ClipStore = 0x22
	Update = 0x23
	Next = 0x24
	Save = 0x25
	Print = 0x26
	MicrophoneEnable = 0x27
	Cine = 0x40
	TransmitPower = 0x41
	Volume = 0x42
	Focus = 0x43
	Depth = 0x44
	SoftStepPrimary = 0x60
	SoftStepSecondary = 0x61
	DepthGainCompensation = 0x70
	ZoomSelect = 0x80
	ZoomAdjust = 0x81
	SpectralDopplerModeSelect = 0x82
	SpectralDopplerAdjust = 0x83
	ColorDopplerModeSelect = 0x84
	ColorDopplerAdjust = 0x85
	MotionModeSelect = 0x86
	MotionModeAdjust = 0x87
	ModeSelect2D = 0x88
	ModeAdjust2D = 0x89
	SoftControlSelect = 0xA0
	SoftControlAdjust = 0xA1


class VendorPage(IntEnum):
	Usage1 = 0x01
	Usage2 = 0x02
	Usage3 = 0x03
	Usage4 = 0x04
	Usage5 = 0x05
	Usage6 = 0x06
	Usage7 = 0x07
	Usage8 = 0x08
	Usage9 = 0x09
	Usage10 = 0x0A
	Usage11 = 0x0B
	Usage12 = 0x0C


class UsagePage(IntEnum):
	GenericDesktopPage = 0x01
	SimulationControlsPage = 0x02
	VRControlsPage = 0x03
	SportControlsPage = 0x04
	GameControlsPage = 0x05
	GenericDeviceControlsPage = 0x06
	KeyboardKeypadPage = 0x07
	LedPage = 0x08
	ButtonPage = 0x09
	OrdinalPage = 0x0A
	TelephonyDevicePage = 0x0B
	ConsumerPage = 0x0C
	DigitizersPage = 0x0D
	AlphanumericDisplayPage = 0x14
	SensorPage = 0x20
	MedicalInstrumentPage = 0x40
	VendorPage = 0xFF00


page_to_enum = {
	UsagePage.GenericDesktopPage : GenericDesktopPage,
	UsagePage.SimulationControlsPage : SimulationControlsPage,
	UsagePage.VRControlsPage : VRControlsPage,
	UsagePage.SportControlsPage : SportControlsPage,
	UsagePage.GameControlsPage : GameControlsPage,
	UsagePage.GenericDeviceControlsPage : GenericDeviceControlsPage,
	UsagePage.KeyboardKeypadPage : KeyboardKeypadPage,
	UsagePage.LedPage : LedPage,
	UsagePage.ButtonPage : ButtonPage,
	UsagePage.OrdinalPage : OrdinalPage,
	UsagePage.TelephonyDevicePage : TelephonyDevicePage,
	UsagePage.ConsumerPage : ConsumerPage,
	UsagePage.DigitizersPage : DigitizersPage,
	UsagePage.AlphanumericDisplayPage : AlphanumericDisplayPage,
	UsagePage.SensorPage : SensorPage,
	UsagePage.MedicalInstrumentPage : MedicalInstrumentPage,
	UsagePage.VendorPage : VendorPage,
}


class SensorEvent(IntEnum):
	Event = 0x00
	SensorState = 0x01
	SensorEvent = 0x02


class HidSensorProperty(IntEnum):
	FriendlyName = 0x01
	PersistentUniqueID = 0x02
	MinimumReportInterval = 0x04
	SensorManufacturer = 0x05
	SensorModel = 0x06
	SensorSerialNumber = 0x07
	SensorDescription = 0x08
	SensorConnectionType = 0x09
	ReportInterval = 0x0E
	ChangeSensitivityAbsolute = 0x0F
	ChangeSensitivityrelativepercent = 0x11
	SensorAccuracy = 0x12
	SensorResolution = 0x13
	RangeMaximum = 0x14
	RangeMinimum = 0x15
	ReportingState = 0x16
	ResponseCurve = 0x18
	PowerState = 0x19


class MotionSensor(IntEnum):
	MotionState = 0x51
	Acceleration = 0x52
	AccelerationAxisX = 0x53
	AccelerationAxisY = 0x54
	AccelerationAxisZ = 0x55
	AngularVelocity = 0x56
	AngularVelocityXAxis = 0x57
	AngularVelocityYAxis = 0x58
	AngularVelocityZAxis = 0x59
	MotionIntensity = 0x5F


class OrientationSensor(IntEnum):
	Heading = 0x71
	HeadingCompensatedMagneticNorth = 0x75
	HeadingCompensatedTrueNorth = 0x76
	HeadingMagneticNorth = 0x77
	HeadingTrueNorth = 0x78
	Distance = 0x79
	DistanceXAxis = 0x7A
	DistanceYAxis = 0x7B
	DistanceZAxis = 0x7C
	DistanceOutOfRange = 0x7D
	Tilt = 0x7E
	TiltXAxis = 0x7F
	TiltYAxis = 0x80
	TiltZAxis = 0x81
	RotationMatrix = 0x82
	Quaternion = 0x83
	MagneticFlux = 0x84
	MagneticFluxXAxis = 0x85
	MagneticFluxYAxis = 0x86
	MagneticFluxZAxis = 0x87
	MagneticAccuracy = 0x88


class LightSensor(IntEnum):
	Illuminance = 0xD1
	ColorTemperature = 0xD2
	Chromaticity = 0xD3
	ChromaticityX = 0xD4
	ChromaticityY = 0xD5


class SensorDataField(IntEnum):
	Electrical = 0x00
	CapacitanceFarads = 0x01
	CurrentAmperes = 0x02
	ElectricalWatts = 0x03
	InductanceHenrys = 0x04
	ResistanceOhms = 0x05
	VoltageVolts = 0x06
	FrequencyHertz = 0x07
	PeriodMilliseconds = 0x08
	PercentOfRange = 0x09
	Custom = 0x40
	CustomUsage = 0x41
	CustomBooleanArray = 0x42
	CustomValue = 0x43
	CustomValue1 = 0x44
	CustomValue2 = 0x45
	CustomValue3 = 0x46
	CustomValue4 = 0x47
	CustomValue5 = 0x48
	CustomValue6 = 0x49
	CustomValue7 = 0x4A
	CustomValue8 = 0x4B
	CustomValue9 = 0x4C
	CustomValue10 = 0x4D
	CustomValue11 = 0x4E
	CustomValue12 = 0x4F
	CustomValue13 = 0x50
	CustomValue14 = 0x51
	CustomValue15 = 0x52
	CustomValue16 = 0x53
	CustomValue17 = 0x54
	CustomValue18 = 0x55
	CustomValue19 = 0x56
	CustomValue20 = 0x57
	CustomValue21 = 0x58
	CustomValue22 = 0x59
	CustomValue23 = 0x5A
	CustomValue24 = 0x5B
	CustomValue25 = 0x5C
	CustomValue26 = 0x5D
	CustomValue27 = 0x5E
	CustomValue28 = 0x5F


class SensorSelector(IntEnum):
	StateUnknown = 0x00
	StateNotAvailable = 0x01
	StateReady = 0x02
	StateNoData = 0x03
	StateInitializing = 0x04
	StateAccessDenied = 0x05
	StateError = 0x06
	EventUnknown = 0x10
	EventStateChanged = 0x11
	EventPropertyChanged = 0x12
	EventDataUpdated = 0x13
	EventPollResponse = 0x14
	EventChangeSensitivity = 0x15
	EventMaxReached = 0x16
	EventMinReached = 0x17
	EventHighThesholdCrossAbove = 0x18
	EventHighThresholdCrossBelow = 0x19
	EventLowThresholdCrossAbove = 0x1a
	EventLowThresholdCrossBelow = 0x1b
	EventZeroThresholdCrossAbove = 0x1c
	EventZeroThresholdCrossBelow = 0x1d
	EventPeriodExceeded = 0x1e
	EventFrequencyExceeded = 0x1f
	EventComplexTrigger = 0x20
	ConnectionTypePCIntegrated = 0x30
	ConnectionTypePCAttached = 0x31
	ConnectionTypePCExternal = 0x32
	PropertyReportingStateNoEvents = 0x40
	PropertyReportingStateAllEvents = 0x41
	PropertyReportingStateThresholdEvents = 0x42
	PropertyReportingStateNoEventsWake = 0x43
	PropertyReportingStateAllEventsWake = 0x44
	PropertyReportingStateThresholdEventsWake = 0x45
	PropertyPowerStateUndefined = 0x50
	PropertyPowerStateD0FullPower = 0x51
	PropertyPowerStateD1LowPower = 0x52
	PropertyPowerStateD2StandbyWithWake = 0x53
	PropertyPowerStateD3SleepWithWake = 0x54
	PropertyPowerStateD4PowerOff = 0x55
	DataFixQualityNoFix = 0x70
	DataFixQualityGps = 0x71
	DataFixQualityDgps = 0x72
	DataFixTypeNoFix = 0x80
	DataFixTypeGpsSpsModeFixValid = 0x81
	DataFixTypeDgpsSpsModeFixValid = 0x82
	DataFixTypeGpsPpsModeFixValid = 0x83
	DataFixTypeRealTimeKinematic = 0x84
	DataFixTypeFloatRtk = 0x85
	DataFixTypeEstimatedDeadReckoning = 0x86
	DataFixTypeManualInputMode = 0x87
	DataFixTypeSimulatorMode = 0x88
	DataGpsOpModeManual = 0x90
	DataGpsOpModeAutomatic = 0x91
	DataGpsSelModeAutonomous = 0xa0
	DataGpsSelModeDgps = 0xa1
	DataGpsSelModeEstimatedDeadReckoning = 0xa2
	DataGpsSelModeManualInput = 0xa3
	DataGpsSelModeSimulator = 0xa4
	DataGpsSelModeDataNotValid = 0xa5
	DataGpsStatusDataValid = 0xb0
	DataGpsStatusDataNotValid = 0xb1
	DesiredAccuracyDefault = 0x60
	DesiredAccuracyHigh = 0x61
	DesiredAccuracyMedium = 0x62
	DesiredAccuracyLow = 0x63
	GorpkKindCategory = 0xd0
	GorpkKindType = 0xd1
	GorpkKindEvent = 0xd2
	GorpkKindProperty = 0xd3
	GorpkKindDatafield = 0xd4


class UnitType(IntEnum):
	NoUnit = 0x00
	SILinear = 0x01
	SIRotation = 0x02
	EnglishLinear = 0x03
	EnglishRotation = 0x04


class Unit(IntEnum):
	Length = 0x01
	Mass = 0x02
	Time = 0x03
	Temperature = 0x04
	Current = 0x05
	LuminousIntensity = 0x06


class ModifierI2a(IntEnum):
	ChangeSensitivityAbsolute = 0x1
	Maximum = 0x2
	Minimum = 0x3
	Accuracy = 0x4
	Resolution = 0x5
	ThresholdHigh = 0x6
	ThresholdLow = 0x7
	CalibrationOffset = 0x8
	CalibrationMultiplier = 0x9
	ReportInterval = 0xA
	FrequencyMax = 0xB
	PeriodMax = 0xC
	ChangeSensitivityPercentOfRange = 0xD
	ChangeSensitivityPercentRelative = 0xE
	VendorOEM = 0xF


class ItemType(IntEnum):
	Constant = 0x1
	Data = 0x2


class ItemLength(IntEnum):
	Variable = 0x1
	Array = 0x2


class ItemBase(IntEnum):
	Relative = 0x1
	Absolute = 0x2
