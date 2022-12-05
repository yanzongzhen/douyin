# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"\xad\x01\n\tPushFrame\x12\r\n\x05seqid\x18\x01 \x01(\x03\x12\r\n\x05logid\x18\x02 \x01(\x03\x12\x0f\n\x07service\x18\x03 \x01(\x03\x12\x0e\n\x06method\x18\x04 \x01(\x03\x12 \n\x0bheadersList\x18\x05 \x03(\x0b\x32\x0b.PushHeader\x12\x18\n\x10palyloadEncoding\x18\x06 \x01(\t\x12\x13\n\x0bpayloadtype\x18\x07 \x01(\t\x12\x10\n\x08palyload\x18\x08 \x01(\x0c\"(\n\nPushHeader\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xea\x01\n\x08Response\x12\x1a\n\x08messages\x18\x01 \x03(\x0b\x32\x08.Message\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\x12\x15\n\rfetchInterval\x18\x03 \x01(\x03\x12\x0b\n\x03now\x18\x04 \x01(\x03\x12\x13\n\x0binternalExt\x18\x05 \x01(\t\x12\x11\n\tfetchType\x18\x06 \x01(\x05\x12&\n\x0brouteParams\x18\x07 \x03(\x0b\x32\x11.RouteParamsEntry\x12\x19\n\x11heartbeatDuration\x18\x08 \x01(\x03\x12\x0f\n\x07needAck\x18\t \x01(\x08\x12\x12\n\npushServer\x18\n \x01(\t\".\n\x10RouteParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"Z\n\x07Message\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\r\n\x05msgId\x18\x03 \x01(\x03\x12\x0f\n\x07msgType\x18\x04 \x01(\x05\x12\x0e\n\x06offset\x18\x05 \x01(\x03\"\xea\x02\n\x0bGiftMessage\x12\x17\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x07.Common\x12\x0e\n\x06giftId\x18\x02 \x01(\x03\x12\x16\n\x0e\x66\x61nTicketCount\x18\x03 \x01(\x03\x12\x12\n\ngroupCount\x18\x04 \x01(\x03\x12\x13\n\x0brepeatCount\x18\x05 \x01(\x03\x12\x12\n\ncomboCount\x18\x06 \x01(\x03\x12\x13\n\x04user\x18\x07 \x01(\x0b\x32\x05.User\x12\x15\n\x06toUser\x18\x08 \x01(\x0b\x32\x05.User\x12\x11\n\trepeatEnd\x18\t \x01(\x05\x12\x0f\n\x07groupId\x18\x0b \x01(\x03\x12\x17\n\x0fincomeTaskgifts\x18\x0c \x01(\x03\x12\x1a\n\x12roomFanTicketCount\x18\r \x01(\x03\x12\x19\n\x04gift\x18\x0f \x01(\x0b\x32\x0b.GiftStruct\x12\r\n\x05logId\x18\x10 \x01(\t\x12\x10\n\x08sendType\x18\x11 \x01(\x03\x12\x1c\n\x14\x62\x61nnedDisplayEffects\x18\x14 \x01(\x03\"\xe1\x01\n\x0b\x43hatMessage\x12\x17\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x07.Common\x12\x13\n\x04user\x18\x02 \x01(\x0b\x32\x05.User\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x17\n\x0fvisibleToSender\x18\x04 \x01(\x08\x12\x1f\n\x0f\x62\x61\x63kgroundImage\x18\x05 \x01(\x0b\x32\x06.Image\x12\x1b\n\x13\x66ullScreenTextColor\x18\x06 \x01(\t\x12!\n\x11\x62\x61\x63kgroundImageV2\x18\x07 \x01(\x0b\x32\x06.Image\x12\x19\n\tgiftImage\x18\n \x01(\x0b\x32\x06.Image\"\xd2\x02\n\x06\x43ommon\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\r\n\x05msgId\x18\x02 \x01(\x03\x12\x0e\n\x06roomId\x18\x03 \x01(\x03\x12\x12\n\ncreateTime\x18\x04 \x01(\x03\x12\x0f\n\x07monitor\x18\x05 \x01(\x05\x12\x11\n\tisShowMsg\x18\x06 \x01(\x08\x12\x10\n\x08\x64\x65scribe\x18\x07 \x01(\t\x12\x10\n\x08\x66oldType\x18\t \x01(\x03\x12\x16\n\x0e\x61nchorFoldType\x18\n \x01(\x03\x12\x15\n\rpriorityScore\x18\x0b \x01(\x03\x12\r\n\x05logId\x18\x0c \x01(\t\x12\x19\n\x11msgProcessFilterK\x18\r \x01(\t\x12\x19\n\x11msgProcessFilterV\x18\x0e \x01(\t\x12\x13\n\x04user\x18\x0f \x01(\x0b\x32\x05.User\x12\x18\n\x10\x61nchorFoldTypeV2\x18\x11 \x01(\x03\x12\x1a\n\x12processAtSeiTimeMs\x18\x12 \x01(\x03\"\xe0\x11\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07shortId\x18\x02 \x01(\x03\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x0e\n\x06gender\x18\x04 \x01(\x05\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\r\n\x05level\x18\x06 \x01(\x05\x12\x10\n\x08\x62irthday\x18\x07 \x01(\x03\x12\x11\n\ttelephone\x18\x08 \x01(\t\x12\x1b\n\x0b\x61vatarThumb\x18\t \x01(\x0b\x32\x06.Image\x12\x1c\n\x0c\x61vatarMedium\x18\n \x01(\x0b\x32\x06.Image\x12\x1b\n\x0b\x61vatarLarge\x18\x0b \x01(\x0b\x32\x06.Image\x12\x10\n\x08verified\x18\x0c \x01(\x08\x12\x12\n\nexperience\x18\r \x01(\x05\x12\x0c\n\x04\x63ity\x18\x0e \x01(\t\x12\x0e\n\x06status\x18\x0f \x01(\x05\x12\x12\n\ncreateTime\x18\x10 \x01(\x03\x12\x12\n\nmodifyTime\x18\x11 \x01(\x03\x12\x0e\n\x06secret\x18\x12 \x01(\x05\x12\x16\n\x0eshareQrcodeUri\x18\x13 \x01(\t\x12\x1a\n\x12incomeSharePercent\x18\x14 \x01(\x05\x12\x1e\n\x0e\x62\x61\x64geImageList\x18\x15 \x01(\x0b\x32\x06.Image\x12\x11\n\tspecialId\x18\x1a \x01(\t\x12\x1c\n\x0c\x61vatarBorder\x18\x1b \x01(\x0b\x32\x06.Image\x12\x15\n\x05medal\x18\x1c \x01(\x0b\x32\x06.Image\x12\x1d\n\rrealTimeIcons\x18\x1d \x01(\x0b\x32\x06.Image\x12 \n\x10newRealTimeIcons\x18\x1e \x01(\x0b\x32\x06.Image\x12\x10\n\x08topVipNo\x18\x1f \x01(\x03\x12\x10\n\x08payScore\x18\" \x01(\x03\x12\x13\n\x0bticketCount\x18# \x01(\x03\x12\x14\n\x0clinkMicStats\x18% \x01(\x05\x12\x11\n\tdisplayId\x18& \x01(\t\x12\x1e\n\x16withCommercePermission\x18\' \x01(\x08\x12\x1b\n\x13withFusionShopEntry\x18( \x01(\x08\x12!\n\x19totalRechargeDiamondCount\x18) \x01(\x03\x12\x17\n\x0fverifiedContent\x18+ \x01(\t\x12\x16\n\x07topFans\x18- \x01(\x0b\x32\x05.User\x12\x0e\n\x06secUid\x18. \x01(\t\x12\x10\n\x08userRole\x18/ \x01(\x05\x12\x1c\n\x0cpersonalCard\x18\x34 \x01(\x0b\x32\x06.Image\x12\x19\n\x11\x61uthorizationInfo\x18\x36 \x01(\x05\x12\"\n\x1a\x61\x64versaryAuthorizationInfo\x18\x37 \x01(\x05\x12#\n\x13mediaBadgeImageList\x18\x39 \x01(\x0b\x32\x06.Image\x12\x1b\n\x13\x61\x64versaryUserStatus\x18: \x01(\x05\x12!\n\x0buserVipInfo\x18; \x01(\x0b\x32\x0c.UserVIPInfo\x12\x14\n\x0clocationCity\x18? \x01(\t\x12\x12\n\nremarkName\x18\x41 \x01(\t\x12\x12\n\nmysteryMan\x18\x42 \x01(\x05\x12\x0e\n\x06webRid\x18\x43 \x01(\t\x12\x1c\n\x14\x64\x65sensitizedNickname\x18\x44 \x01(\t\x12\x17\n\x0e\x61llowBeLocated\x18\xe9\x07 \x01(\x08\x12\x1c\n\x13\x61llowFindByContacts\x18\xea\x07 \x01(\x08\x12!\n\x18\x61llowOthersDownloadVideo\x18\xeb\x07 \x01(\x08\x12,\n#allowOthersDownloadWhenSharingVideo\x18\xec\x07 \x01(\x08\x12\x1e\n\x15\x61llowShareShowProfile\x18\xed\x07 \x01(\x08\x12\x1a\n\x11\x61llowShowInGossip\x18\xee\x07 \x01(\x08\x12\x1a\n\x11\x61llowShowMyAction\x18\xef\x07 \x01(\x08\x12\x1c\n\x13\x61llowStrangeComment\x18\xf0\x07 \x01(\x08\x12\x1f\n\x16\x61llowUnfollowerComment\x18\xf1\x07 \x01(\x08\x12\x18\n\x0f\x61llowUseLinkmic\x18\xf2\x07 \x01(\x08\x12\x1a\n\tavatarJpg\x18\xf4\x07 \x01(\x0b\x32\x06.Image\x12\x11\n\x08\x62gImgUrl\x18\xf5\x07 \x01(\t\x12\x1c\n\x13\x62irthdayDescription\x18\xf6\x07 \x01(\t\x12\x16\n\rbirthdayValid\x18\xf7\x07 \x01(\x08\x12\x14\n\x0b\x62lockStatus\x18\xf8\x07 \x01(\x05\x12\x18\n\x0f\x63ommentRestrict\x18\xf9\x07 \x01(\x05\x12\x16\n\rconstellation\x18\xfa\x07 \x01(\t\x12\x15\n\x0c\x64isableIchat\x18\xfb\x07 \x01(\x05\x12\x17\n\x0e\x65nableIchatImg\x18\xfc\x07 \x01(\x03\x12\x0c\n\x03\x65xp\x18\xfd\x07 \x01(\x05\x12\x17\n\x0e\x66\x61nTicketCount\x18\xfe\x07 \x01(\x03\x12\x19\n\x10\x66oldStrangerChat\x18\xff\x07 \x01(\x08\x12\x15\n\x0c\x66ollowStatus\x18\x80\x08 \x01(\x03\x12\x18\n\x0fhotsoonVerified\x18\x81\x08 \x01(\x08\x12\x1e\n\x15hotsoonVerifiedReason\x18\x82\x08 \x01(\t\x12\x1a\n\x11ichatRestrictType\x18\x83\x08 \x01(\x05\x12\x0e\n\x05idStr\x18\x84\x08 \x01(\t\x12\x13\n\nisFollower\x18\x85\x08 \x01(\x08\x12\x14\n\x0bisFollowing\x18\x86\x08 \x01(\x08\x12\x19\n\x10needProfileGuide\x18\x87\x08 \x01(\x08\x12\x12\n\tpayScores\x18\x88\x08 \x01(\x03\x12\x1a\n\x11pushCommentStatus\x18\x89\x08 \x01(\x08\x12\x11\n\x08pushDigg\x18\x8a\x08 \x01(\x08\x12\x13\n\npushFollow\x18\x8b\x08 \x01(\x08\x12\x19\n\x10pushFriendAction\x18\x8c\x08 \x01(\x08\x12\x12\n\tpushIchat\x18\x8d\x08 \x01(\x08\x12\x13\n\npushStatus\x18\x8e\x08 \x01(\x08\x12\x16\n\rpushVideoPost\x18\x8f\x08 \x01(\x08\x12\x1b\n\x12pushVideoRecommend\x18\x90\x08 \x01(\x08\x12\x1a\n\x05stats\x18\x91\x08 \x01(\x0b\x32\n.UserStats\x12\x17\n\x0everifiedMobile\x18\x92\x08 \x01(\x08\x12\x17\n\x0everifiedReason\x18\x93\x08 \x01(\t\x12$\n\x1bwithCarManagementPermission\x18\x94\x08 \x01(\x08\"\x80\x01\n\x05Image\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\r\n\x05width\x18\x04 \x01(\x03\x12\x10\n\x08\x61vgColor\x18\x05 \x01(\t\x12\x11\n\timageType\x18\x06 \x01(\x05\x12\x12\n\nopenWebUrl\x18\x07 \x01(\t\x12\x12\n\nisAnimated\x18\t \x01(\x08\"y\n\nFollowInfo\x12\x16\n\x0e\x66ollowingCount\x18\x01 \x01(\x03\x12\x15\n\rfollowerCount\x18\x02 \x01(\x03\x12\x14\n\x0c\x66ollowStatus\x18\x03 \x01(\x03\x12\x12\n\npushStatus\x18\x04 \x01(\x03\x12\x12\n\nremarkName\x18\x05 \x01(\t\"\xd6\x02\n\x08PayGrade\x12\x19\n\x11totalDiamondCount\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08nextName\x18\x05 \x01(\t\x12\r\n\x05level\x18\x06 \x01(\x03\x12\x13\n\x0bnextDiamond\x18\x08 \x01(\x03\x12\x12\n\nnowDiamond\x18\t \x01(\x03\x12\x1b\n\x13thisGradeMinDiamond\x18\n \x01(\x03\x12\x1b\n\x13thisGradeMaxDiamond\x18\x0b \x01(\x03\x12\x15\n\rpayDiamondBak\x18\x0c \x01(\x03\x12\x15\n\rgradeDescribe\x18\r \x01(\t\x12\x16\n\x0escreenChatType\x18\x0f \x01(\x03\x12\x1a\n\x12upgradeNeedConsume\x18\x15 \x01(\x03\x12\x16\n\x0enextPrivileges\x18\x16 \x01(\t\x12\r\n\x05score\x18\x19 \x01(\x03\x12\x14\n\x0bgradeBanner\x18\xe9\x07 \x01(\t\"\xad\x01\n\x0bUserVIPInfo\x12\x10\n\x08vipLevel\x18\x01 \x01(\x03\x12\x14\n\x0cvipLevelName\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x11\n\tstartTime\x18\x04 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x05 \x01(\x03\x12\x15\n\rremainingDays\x18\x06 \x01(\x03\x12\x14\n\x0ctotalConsume\x18\x07 \x01(\x03\x12\x15\n\rtargetConsume\x18\x08 \x01(\x03\"\xad\x02\n\tUserStats\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05idStr\x18\x02 \x01(\t\x12\x16\n\x0e\x66ollowingCount\x18\x03 \x01(\x03\x12\x15\n\rfollowerCount\x18\x04 \x01(\x03\x12\x13\n\x0brecordCount\x18\x05 \x01(\x03\x12\x15\n\rtotalDuration\x18\x06 \x01(\x03\x12\x1b\n\x13\x64\x61ilyFanTicketCount\x18\x07 \x01(\x03\x12\x13\n\x0b\x64\x61ilyIncome\x18\x08 \x01(\x03\x12\x11\n\titemCount\x18\t \x01(\x03\x12\x19\n\x11\x66\x61voriteItemCount\x18\n \x01(\x03\x12\x14\n\x0c\x64iamondCount\x18\x0b \x01(\x03\x12\x1c\n\x14\x64iamondConsumedCount\x18\x0c \x01(\x03\x12\x16\n\x0etuwenItemCount\x18\r \x01(\x03\"\xf4\x07\n\nGiftStruct\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\x12\x10\n\x08\x64\x65scribe\x18\x02 \x01(\t\x12\x0e\n\x06notify\x18\x03 \x01(\x08\x12\x10\n\x08\x64uration\x18\x04 \x01(\x03\x12\n\n\x02id\x18\x05 \x01(\x03\x12\x12\n\nforLinkmic\x18\x07 \x01(\x08\x12\x0e\n\x06\x64oodle\x18\x08 \x01(\x08\x12\x13\n\x0b\x66orFansclub\x18\t \x01(\x08\x12\r\n\x05\x63ombo\x18\n \x01(\x08\x12\x0c\n\x04type\x18\x0b \x01(\x05\x12\x14\n\x0c\x64iamondCount\x18\x0c \x01(\x05\x12\x1a\n\x12isDisplayedOnPanel\x18\r \x01(\x08\x12\x17\n\x0fprimaryEffectId\x18\x0e \x01(\x03\x12\x1d\n\rgiftLabelIcon\x18\x0f \x01(\x0b\x32\x06.Image\x12\x0c\n\x04name\x18\x10 \x01(\t\x12\x0e\n\x06region\x18\x11 \x01(\t\x12\x0e\n\x06manual\x18\x12 \x01(\t\x12\x11\n\tforCustom\x18\x13 \x01(\x08\x12\x14\n\x04icon\x18\x15 \x01(\x0b\x32\x06.Image\x12\x12\n\nactionType\x18\x16 \x01(\x05\x12\x17\n\x0fwatermelonSeeds\x18\x17 \x01(\x05\x12\x12\n\ngoldEffect\x18\x18 \x01(\t\x12\x13\n\x0bgoldenBeans\x18\x1a \x01(\x03\x12\x12\n\nhonorLevel\x18\x1b \x01(\x03\x12\x10\n\x08itemType\x18\x1c \x01(\x05\x12\x11\n\tschemeUrl\x18\x1d \x01(\t\x12\x11\n\teventName\x18\x1f \x01(\t\x12\x12\n\nnobleLevel\x18  \x01(\x03\x12\x10\n\x08guideUrl\x18! \x01(\t\x12\x16\n\x0epunishMedicine\x18\" \x01(\x08\x12\x11\n\tforPortal\x18# \x01(\x08\x12\x14\n\x0c\x62usinessText\x18$ \x01(\t\x12\x0f\n\x07\x63nyGift\x18% \x01(\x08\x12\r\n\x05\x61ppId\x18& \x01(\x03\x12\x10\n\x08vipLevel\x18\' \x01(\x03\x12\x0e\n\x06isGray\x18( \x01(\x08\x12\x15\n\rgraySchemeUrl\x18) \x01(\t\x12\x11\n\tgiftScene\x18* \x01(\x03\x12\x18\n\x10\x66orFirstRecharge\x18. \x01(\x08\x12%\n\x15\x64ynamicImgForSelected\x18/ \x01(\x0b\x32\x06.Image\x12\x17\n\x0f\x61\x66terSendAction\x18\x30 \x01(\x05\x12\x17\n\x0fgiftOfflineTime\x18\x31 \x01(\x03\x12\x12\n\ntopBarText\x18\x32 \x01(\t\x12\x1e\n\x0etopRightAvatar\x18\x33 \x01(\x0b\x32\x06.Image\x12\x17\n\x0f\x62\x61nnerSchemeUrl\x18\x34 \x01(\t\x12\x10\n\x08isLocked\x18\x35 \x01(\x08\x12\x14\n\x0creqExtraType\x18\x36 \x01(\x03\x12\x1b\n\x13needSweepLightCount\x18: \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PUSHFRAME._serialized_start=18
  _PUSHFRAME._serialized_end=191
  _PUSHHEADER._serialized_start=193
  _PUSHHEADER._serialized_end=233
  _RESPONSE._serialized_start=236
  _RESPONSE._serialized_end=470
  _ROUTEPARAMSENTRY._serialized_start=472
  _ROUTEPARAMSENTRY._serialized_end=518
  _MESSAGE._serialized_start=520
  _MESSAGE._serialized_end=610
  _GIFTMESSAGE._serialized_start=613
  _GIFTMESSAGE._serialized_end=975
  _CHATMESSAGE._serialized_start=978
  _CHATMESSAGE._serialized_end=1203
  _COMMON._serialized_start=1206
  _COMMON._serialized_end=1544
  _USER._serialized_start=1547
  _USER._serialized_end=3819
  _IMAGE._serialized_start=3822
  _IMAGE._serialized_end=3950
  _FOLLOWINFO._serialized_start=3952
  _FOLLOWINFO._serialized_end=4073
  _PAYGRADE._serialized_start=4076
  _PAYGRADE._serialized_end=4418
  _USERVIPINFO._serialized_start=4421
  _USERVIPINFO._serialized_end=4594
  _USERSTATS._serialized_start=4597
  _USERSTATS._serialized_end=4898
  _GIFTSTRUCT._serialized_start=4901
  _GIFTSTRUCT._serialized_end=5913
# @@protoc_insertion_point(module_scope)
