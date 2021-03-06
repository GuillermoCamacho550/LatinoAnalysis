
Productions = { 
   
   'summer16_nAOD_v1' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1.py' ,
                          'cmssw'   : 'Full2016' ,  
                          'year'    : '2016' , 
                          'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                          'YRver'   : ['YR4','13TeV'] ,
                        },

   'summer16_nAOD_v1_test' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1_test.py' ,
                          'cmssw'   : 'Full2016' ,
                          'year'    : '2016' , 
                          'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                          'YRver'   : ['YR4','13TeV'] ,
                        },                    

   'Run2017_nAOD_v1_Study2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                         'year'    : '2017' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },

   'Fall2017_nAOD_v1_Study2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                         'year'    : '2017' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },               

   'Run2018_nAOD_v1_Study2018':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_nAOD_v1.py' ,
                         'cmssw'   : 'Full2018' ,
                         'year'    : '2018' ,
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' , ## for the moment just copy 'samplesCrossSections2017.py'
                         'YRver'   : ['YR4','13TeV'] ,
                   },


   # ---- BAD electron ID: 

   'Run2017_nAOD_v1_Full2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                         'year'    : '2017' , 
                   },

   'Fall2017_nAOD_v1_Full2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                         'year'    : '2017' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },     

################################### nAODv2 : 2017v2 ######################################

 # -------- 2016 DATA 94X nAODv3
 'Run2016_94X_nAODv2_Full2016v2': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv2.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' ,
                   },



  # ---- Relaxed loose ID / misHit / ...

   'Run2017_nAOD_v1_Full2017v2':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2' ,
                         'year'    : '2017' , 
                   },

   'Fall2017_nAOD_v1_Full2017v2':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2' ,
                         'year'    : '2017' , 
                         'JESGT'   : 'Fall17_17Nov2017_V6_MC' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },           

################################### nAODv3 ######################################

 # -------- 2016 DATA 94X nAODv3
 'Run2016_94X_nAODv3_Full2016v2': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv3.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' , 
                   },

 # -------- 2016 MC 94X nAODv3
 'Summer16_94X_nAODv3_Full2016v2': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_94X_nAODv3.py' ,
                       'cmssw'   : 'Full2016v2' ,
                       'year'    : '2016' , 
                       'JESGT'   : 'Summer16_23Sep2016V4_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

################################### nAODv4 ######################################

 # -------- 2016 DATA 102X nAODv4
 'Run2016_102X_nAODv4_Full2016v2': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' , 
                   }, 

 # -------- 2017 DATA 102X nAODv4 (TODO: samples/Run2017_102X_nAODv4.py)
 'Run2017_102X_nAODv4_Full2017v3': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2017v3',
                       'year'    : '2017' , 
                   },

 # -------- 2018 DATA 102X nAODv4 - 14Sep2018 production
 'Run2018_102X_nAODv4_14Sep_Full2018' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv4_14Sep2018.py' ,
                       'cmssw'   : 'Full2018',
                       'year'    : '2018' ,
                   },

 # -------- 2018 DATA 102X nAODv4 - 14Dec2018 production
 'Run2018_102X_nAODv4_14Dec_Full2018' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv4_14Dec2018.py' ,
                       'cmssw'   : 'Full2018',
                       'year'    : '2018' ,
                   },

 # -------- 2018 MC 102X nAODv4
 'Autumn18_102X_nAODv4_Full2018': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2018' ,
                       'year'    : '2018' ,
                   #   'JESGT'   : 'Summer16_23Sep2016V4_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

}
