---
title: "v8 scons error"
layout: post
date: "2010-06-06"
categories: [tech]
---

While trying to install Google v8, I had an error:

    v8-read-only$ scons
    scons: Reading SConscript files ...
    scons: done reading SConscript files.
    scons: Building targets ...
    g++ -o obj/release/api.o -c -Wall -Werror -W -Wno-unused-parameter -Wnon-virtual-dtor -pedantic -m32 -O3 -fomit-frame-pointer -fdata-sections -ffunction-sections -ansi -fno-rtti -fno-exceptions -fvisibility=hidden -Wall -Werror -W -Wno-unused-parameter -Wnon-virtual-dtor -pedantic -m32 -O3 -fomit-frame-pointer -fdata-sections -ffunction-sections -ansi -DV8_TARGET_ARCH_IA32 -DENABLE_VMSTATE_TRACKING -DENABLE_LOGGING_AND_PROFILING -DENABLE_DEBUGGER_SUPPORT -Isrc src/api.cc
    cc1plus: warnings being treated as errors
    src/handles-inl.h: In static member function 'static void v8::V8::RemoveMessageListeners(void (*)(v8::Handle<v8::Message>, v8::Handle<v8::Value>))':
    src/handles-inl.h:50: error: dereferencing pointer '<anonymous>' does break strict-aliasing rules
    src/handles-inl.h:50: error: dereferencing pointer '<anonymous>' does break strict-aliasing rules
    src/utils.h:739: note: initialized from here
    cc1plus: error: dereferencing pointer 'dest' does break strict-aliasing rules
    cc1plus: error: dereferencing pointer 'dest' does break strict-aliasing rules
    cc1plus: error: dereferencing pointer 'dest' does break strict-aliasing rules
    cc1plus: error: dereferencing pointer 'dest' does break strict-aliasing rules
    src/api.cc:3767: note: initialized from here
    scons: *** [obj/release/api.o] Error 1
    scons: building terminated because of error


Solved by using export GCC_VERSION=44, before running scons.
