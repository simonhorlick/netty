licenses(['notice'])
package(default_visibility = ['//visibility:public'])

java_library(
  name = 'buffer',
  srcs = glob([
    'buffer/src/main/**/*.java'
  ]),
  deps = [
    ':common'
  ],
)

java_library(
  name = 'codec',
  srcs = glob([
    'codec/src/main/**/*.java'
  ], exclude=[
    # This depends on org.jboss.marshalling:jboss-marshalling
    'codec/src/main/java/io/netty/handler/codec/marshalling/*.java',
    # com.jcraft:jzlib
    'codec/src/main/java/io/netty/handler/codec/compression/JZlib*.java',
    'codec/src/main/java/io/netty/handler/codec/compression/ZlibUtil.java',
    'codec/src/main/java/io/netty/handler/codec/compression/ZlibCodecFactory.java',
    # com.github.jponge:lzma-java
    'codec/src/main/java/io/netty/handler/codec/compression/Lzma*.java',
    # com.ning:compress-lzf
    'codec/src/main/java/io/netty/handler/codec/compression/Lzf*.java',
    # net.jpountz.lz4
    'codec/src/main/java/io/netty/handler/codec/compression/Lz4*.java',
  ]),
  deps = [
    ':buffer',
    ':common',
    ':transport',
    '//external:protobuf_java_lib',
  ],
)

# Generate collections code
py_binary(
  name = 'codegen',
  srcs = [
    'common/src/main/script/codegen.py'
  ],
  data = [
    'common/src/main/templates/io/netty/util/collection/KObjectMap.template',
    'common/src/main/templates/io/netty/util/collection/KObjectHashMap.template',
  ],
)

genrule(
  name = 'codegen_collection',
  tools = [
    ':codegen'
  ],
  cmd = '$(location :codegen) --output=$(@D)',
  outs = [
    'ByteObjectHashMap.java',
    'ByteObjectMap.java',
    'CharObjectHashMap.java',
    'CharObjectMap.java',
    'IntObjectHashMap.java',
    'IntObjectMap.java',
    'LongObjectHashMap.java',
    'LongObjectMap.java',
    'ShortObjectHashMap.java',
    'ShortObjectMap.java',
  ]
)

java_library(
  name = 'common',
  srcs = glob([
    'common/src/main/**/*.java'
  ]) + [
    ':codegen_collection',
  ],
  deps = [
    '//third_party/java/commons-logging',
    '//third_party/java/javassist',
    '//third_party/java/log4j',
    '//third_party/java/slf4j'
  ],
)

java_library(
  name = 'resolver',
  srcs = glob([
    'resolver/src/main/**/*.java'
  ]),
  deps = [
    ':buffer',
    ':common',
  ],
)

java_library(
  name = 'transport',
  srcs = glob([
    'transport/src/main/**/*.java'
  ]),
  deps = [
    ':buffer',
    ':common',
    ':resolver',
  ],
)

java_library(
  name = 'netty',
  exports = [
    'buffer',
    'codec',
    'common',
    'resolver',
    'transport',
  ]
)
