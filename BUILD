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
    '//external:jzlib',
    '//external:protobuf_java_lib',
  ],
)

java_library(
  name = 'codec-http',
  srcs = glob([
    'codec-http/src/main/**/*.java'
  ], exclude=[
    # This depends ssl support in handler.
    'codec-http/src/main/java/io/netty/handler/codec/http/websocketx/*.java',
  ]),
  deps = [
    ':buffer',
    ':codec',
    ':common',
    ':handler',
    ':transport',
    '//external:jzlib',
  ],
)

java_library(
  name = 'codec-http2',
  srcs = glob([
    'codec-http2/src/main/**/*.java'
  ]),
  deps = [
    ':buffer',
    ':codec',
    ':codec-http',
    ':common',
    ':handler',
    ':transport',
    '//external:hpack',
  ],
)

# Generate collections code
py_binary(
  name = 'codegen',
  srcs = [
    'common/src/main/script/codegen.py'
  ],
  data = [
    'common/src/main/templates/io/netty/util/collection/KCollections.template',
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
    'ByteCollections.java',
    'CharObjectHashMap.java',
    'CharObjectMap.java',
    'CharCollections.java',
    'IntObjectHashMap.java',
    'IntObjectMap.java',
    'IntCollections.java',
    'LongObjectHashMap.java',
    'LongObjectMap.java',
    'LongCollections.java',
    'ShortObjectHashMap.java',
    'ShortObjectMap.java',
    'ShortCollections.java',
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
    '//external:apache-commons-logging',
    '//external:apache-log4j',
    '//external:javassist',
    '//external:slf4j'
  ],
)

java_library(
  name = 'handler',
  srcs = glob([
    'handler/src/main/**/*.java'
  ], exclude=[
    'handler/src/main/java/io/netty/handler/ssl/util/Bouncy*.java',
    'handler/src/main/java/io/netty/handler/ssl/util/*SelfSign*.java',
  ]),
  deps = [
    ':buffer',
    ':codec',
    ':common',
    ':transport',
    '//external:jetty-alpn',
    '//external:jetty-npn',
    '//external:netty-tcnative',
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
    'codec-http',
    'codec-http2',
    'common',
    'handler',
    'resolver',
    'transport',
  ]
)
