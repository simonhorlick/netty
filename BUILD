licenses(["notice"])

package(default_visibility = ["//visibility:public"])

java_library(
    name = "buffer",
    srcs = glob([
        "buffer/src/main/**/*.java",
    ]),
    javacopts = [
        "-Xlint:none",
        "-extra_checks:off",
    ],
    deps = [
        ":common",
    ],
)

java_library(
    name = "codec",
    srcs = glob(
        [
            "codec/src/main/**/*.java",
        ],
        exclude = [
            # This depends on org.jboss.marshalling:jboss-marshalling
            "codec/src/main/java/io/netty/handler/codec/marshalling/*.java",
            # com.github.jponge:lzma-java
            "codec/src/main/java/io/netty/handler/codec/compression/Lzma*.java",
            # com.ning:compress-lzf
            "codec/src/main/java/io/netty/handler/codec/compression/Lzf*.java",
            # net.jpountz.lz4
            "codec/src/main/java/io/netty/handler/codec/compression/Lz4*.java",
        ],
    ),
    # FastLz.java:217: error: [IdentityBinaryExpression] Writing `a ||
    # a` is equivalent to `a`
    javacopts = [
        "-extra_checks:off",
    ],
    deps = [
        ":buffer",
        ":common",
        ":transport",
        "@com_google_protobuf//:protobuf_java",
        "@com_google_protobuf//:protobuf_javanano",
        "@com_jcraft_jzlib//jar",
    ],
)

java_library(
    name = "codec-http",
    srcs = glob([
        "codec-http/src/main/**/*.java",
    ]),
    deps = [
        ":buffer",
        ":codec",
        ":common",
        ":handler",
        ":transport",
        "@com_jcraft_jzlib//jar",
    ],
)

java_library(
    name = "codec-http2",
    srcs = glob([
        "codec-http2/src/main/**/*.java",
    ]),
    deps = [
        ":buffer",
        ":codec",
        ":codec-http",
        ":common",
        ":handler",
        ":transport",
    ],
)

# Generate collections code
py_binary(
    name = "codegen",
    srcs = [
        "common/src/main/script/codegen.py",
    ],
    data = [
        "common/src/main/templates/io/netty/util/collection/KCollections.template",
        "common/src/main/templates/io/netty/util/collection/KObjectHashMap.template",
        "common/src/main/templates/io/netty/util/collection/KObjectMap.template",
    ],
)

genrule(
    name = "codegen_collection",
    outs = [
        "ByteObjectHashMap.java",
        "ByteObjectMap.java",
        "ByteCollections.java",
        "CharObjectHashMap.java",
        "CharObjectMap.java",
        "CharCollections.java",
        "IntObjectHashMap.java",
        "IntObjectMap.java",
        "IntCollections.java",
        "LongObjectHashMap.java",
        "LongObjectMap.java",
        "LongCollections.java",
        "ShortObjectHashMap.java",
        "ShortObjectMap.java",
        "ShortCollections.java",
    ],
    cmd = "$(location :codegen) --output=$(@D)",
    tools = [
        ":codegen",
    ],
)

java_library(
    name = "common",
    srcs = glob([
        "common/src/main/**/*.java",
    ]) + [
        ":codegen_collection",
    ],
    deps = [
        "@apache_commons_logging//jar",
        "@javassist//jar",
        "@org_apache_log4j_log4j//jar",
        "@org_apache_logging_log4j_log4j_api//jar",
        "@org_jctools_jctools_core//jar",
        "@org_slf4j_slf4j_api//jar",
    ],
)

java_library(
    name = "handler",
    srcs = glob([
        "handler/src/main/**/*.java",
    ]),
    # SslContext.java:881: error: [InsecureCipherMode] Insecure usage of
    # Cipher.getInstance(): the transformation is not a compile-time
    # constant expression.
    javacopts = [
        "-extra_checks:off",
    ],
    deps = [
        ":buffer",
        ":codec",
        ":common",
        ":transport",
        "@io_netty_netty_tcnative_boringssl_static//jar",
        "@org_bouncycastle_bcpkix_jdk15on//jar",
        "@org_bouncycastle_bcprov_jdk15on//jar",
        "@org_eclipse_jetty_alpn_alpn_api//jar",
        "@org_eclipse_jetty_npn_npn_api//jar",
    ],
)

java_library(
    name = "resolver",
    srcs = glob([
        "resolver/src/main/**/*.java",
    ]),
    deps = [
        ":buffer",
        ":common",
    ],
)

java_library(
    name = "transport",
    srcs = glob([
        "transport/src/main/**/*.java",
    ]),
    javacopts = [
        "-extra_checks:off",
    ],
    deps = [
        ":buffer",
        ":common",
        ":resolver",
    ],
)

java_library(
    name = "transport-native-epoll",
    srcs = glob([
        "transport-native-epoll/src/main/**/*.java",
    ]),
    deps = [
        ":buffer",
        ":common",
        ":resolver",
        ":transport",
    ],
)

java_library(
    name = "netty",
    exports = [
        "buffer",
        "codec",
        "codec-http",
        "codec-http2",
        "common",
        "handler",
        "resolver",
        "transport",
    ],
)
