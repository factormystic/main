#####################################################################################
#
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
# This source code is subject to terms and conditions of the Apache License, Version 2.0. A 
# copy of the license can be found in the License.html file at the root of this distribution. If 
# you cannot locate the  Apache License, Version 2.0, please send an email to 
# ironpy@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
# by the terms of the Apache License, Version 2.0.
#
# You must not remove this notice, or any other, from this software.
#
#
#####################################################################################
    
from iptest.assert_util import *


add_clr_assemblies("loadorder_2")

# namespace First {
#     public class Nongeneric1 {
#         public static string Flag = typeof(Nongeneric1).FullName;
#     }
# }

import First
from First import *

add_clr_assemblies("loadorder_2d")

# // non-generic type, which has same namespace, different name from First.Nongeneric1
# namespace First {
#     public class Nongeneric2 {
#         public static string Flag = typeof(Nongeneric2).FullName;
#     }
# }

AreEqual(First.Nongeneric2.Flag, "First.Nongeneric2")
AreEqual(First.Nongeneric1.Flag, "First.Nongeneric1")

AreEqual(Nongeneric1.Flag, "First.Nongeneric1")
AssertError(NameError, lambda: Nongeneric2)

from First import *

AreEqual(Nongeneric1.Flag, "First.Nongeneric1")
AreEqual(Nongeneric2.Flag, "First.Nongeneric2")

