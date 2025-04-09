$ This is a LS-Dyna deck to test PrePyna
$ This test contains a mixture of test keywords:
$      - test_scalar
$      - test_scalar_optional
$      - test_mixed
$      - test_mixed_optional
*TEST_SCALAR
$#                                                                                   title
                                           Test of scalar variables without optional cards
$#    svip      svin     svfps     svfns     svfpl     svfnl  svfpsmal  svfnsmal     svstr
         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon
$ This is a comment in the middle
$ PrePyna should conserve both comment lines
*TEST_SCALAR_OPTIONAL
$#                                                                                   title
                                              Test of scalar variables with optional cards
$#      id     trig2     var23     var24     var25     var26     var27     var28     var29
         1         1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon
$#   var31     trig3     var33     var34     var35     var36     var37     var38     var39
         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon
*TEST_MIXED
$#                                                                                   title
                                            Test of mixed variables without optional cards
$#     kid        v1        v2        v3        v4        v5        v6        v7        v8
         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon
$#     vv0       vv1       vv2       vv3       vv4       vv5       vv6       vv7       vv8
         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_str
         2        -2         2        -22.3457E+10-2.346E+102.3457E-12-2.346E-12random_str
*TEST_MIXED_OPTIONAL
$#                                                                                   title
                                               Test of mixed variables with optional cards
$#     kid     trig2     var23     var24     var25     var26     var27     var28     var29
         1         1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon
$#   var31     trig3     var33     var34     var35     var36     var37     var38     var39
         1         1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_lon
$#   var41     trig4     var43     var44     var45     var46     var47     var48     var49
         1        -1         1        -11.2346E+10-1.235E+101.2346E-12-1.235E-12random_str
         2        -2         2        -22.3457E+10-2.346E+102.3457E-12-2.346E-12random_str
*END
