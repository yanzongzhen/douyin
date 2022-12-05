from protobuf import message_pb2
# import message_pb2
import gzip
import json
from google.protobuf.json_format import MessageToDict
# hex来自上方的粘贴
hex = '08b40d10efdef3c8d7f1cdb67618b84520082a150a0d636f6d70726573735f747970651204677a69702ab9020a0f696d2d696e7465726e616c5f65787412a502696e7465726e616c5f7372633a707573687365727665727c7773735f707573685f726f6f6d5f69643a373137333530373837333735323839343234357c7773735f707573685f6469643a373137323832323939303731383235363634387c7773735f707573685f6c6f675f69643a383533333533373934393639383831333830377c7773735f66657463685f6d733a313637303231353936343831357c7773735f707573685f6d733a313637303231353936343937357c7773735f6d73675f747970653a727c777264735f6b76733a57656263617374526f6f6d52616e6b4d6573736167652d313637303231353936343036353131313039335f57656263617374526f6f6d53746174734d6573736167652d313637303231353935393134373838363135332a4e0a09696d2d637572736f721241742d313637303231353936343937355f722d373137333532323934323633373137383133375f642d315f752d315f682d315f6368642d5f6368752d5f7264632d312a170a06696d2d6e6f77120d313637303231353936343937352a190a0e696d2d6c6976655f637572736f721207642d315f752d31320270623a036d73674286071f8b08000000000000ffc494d16b1c451cc73349688e256838508ef872c43761ef66767677760f442f6a5ae3a56d925e4c8a32ccedceeddde5f676bbb377972b451a69d523512c1611ab50526b4a4bd18616f5c007fb50d007ff00051f24b93b8b4f79101f25976863c9833e888fc3f7cbf733f31d7e3fe97c448abecc731613e17305164e712198c3a39b4352e22061e4cab56bbf7dbbf6d33d2b76f5fde6b9df7ffde19e05c1fc57db20ba3a14f9f1ee9d959fc1c8cde6d9c8e8639daf2fb49757ba6b37dacd37375b17b7beb8dd7e67350e20986c48f54218fa22954cfa38617bd546b1e217ad84e5b94956e72e4f2208971084bb2799d558c88264e809d9aac845191a0853236fea04e75588ac9c8a957c0e41cdce31ac738561943313259f3bcfe403cf7d5a85086a18416c5c074bd2891d760f2dd777dff7d0158aae93dc539255c103ea04cce6b4cc6bbc4c6b1a4509bfe2bc16fae59aece54a89a2cb1c1e1b89c721181f8d81b1c7bb6f5fe95e6f766e363bad75d469ad6fadac746e5cde0043915b60a43f065ae01b00c187e095fff22a6be05529fb6fe27b55539f35f618ca1245543d287f383e0cc15d204991b143d260a42fdaf77a7fdf467f04e984182ac2dbfd646a56ad674ae9f1743a9d96b39963b3d3f32f34e62cff74c675eacf971be4a5ec117bcee0b90505be58ca90e3a5d95cfdd8d4e70303f707feb71fba3fc0a5e93fd1fa3fa9ac6215bc80e65945d09039b4a61cc0854f8e3f3236dcd9686e7ef9f12ee7dd41b03678f0787c377878b7baa3f32c7bca2956a7b30bac2a268e4ef8a71620cb68a52cae64d3b07cf2c4e1b06acc2de8e368223d8533a78feb9393d33359172fced472276d6bf489f6c5cfdaabcb5b9fac6f7d70bbdd7cef97b397db6f5de87ebabcd97a63b26fe9d2f69d8f0ec5fe9ae6683a94914ea0823453570d85d0402688604d514c55d13141c44098505b46b42a235a9011b50ab64cad4255a6816dc928d61d8a5fba75eefcf7f0a9abfdc54ac8830a2b53115829bf2a0a8207351e9ca90b41778e34f03c9716ed540f02894130d114c35415557b60b2770c50d1346c621d6a44554d8890f9c050f69c9d1043c358c3c4544ddd340ca4a89adaf3e4796815a82b52fb9e86f6e5ff5d51484f718543c386cf53c1997a600bba5813a9bd4538e379ee0cab2cee2dc37d8d415d43084113d37dd6d99085e261af66229518868e34fceca347c01f000000ffff010000ffff340cb61881050000'

data = bytes.fromhex(hex)
o = message_pb2.PushFrame()
o.ParseFromString(data)

payload = gzip.decompress(o.palyload)
r = message_pb2.Response()
r.ParseFromString(payload)
print(r)
e = r
messagelist = e.messages
for t in messagelist:
    o = t.payload
    message_ = ''
    if t.method == "WebcastLikeMessage":
        message_ = message_pb2.LikeMessage()
        message_.ParseFromString(o)
    elif t.method == "WebcastChatMessage":
        message_ = message_pb2.ChatMessage()
        message_.ParseFromString(o)
    elif t.method == "WebcastMemberMessage":
        message_ = message_pb2.MemberMessage()
        message_.ParseFromString(o)
    elif t.method == "WebcastSocialMessage":
        message_ = message_pb2.SocialMessage()
        message_.ParseFromString(o)
    elif t.method == "WebcastGiftMessage":
        message_ = message_pb2.GiftMessage()
        message_.ParseFromString(o)
    else:
        print(t.method)
    if message_:
        obj1 = MessageToDict(message_, preserving_proto_field_name=True)
        print(json.dumps(obj1, ensure_ascii=False))
