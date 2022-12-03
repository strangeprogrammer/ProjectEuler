FEXISTS=$(shell [ -e $(1) ] && echo true || echo false)

ifeq (true,$(call FEXISTS,memoize.py))
MEMOIZE_PY:=../tools/memoize.py
endif

ifeq (true,$(call FEXISTS,primes.py))
PRIMES_PY:=../tools/primes.py
endif

ifeq (true,$(call FEXISTS,gentools.py))
GENTOOLS_PY:=../tools/gentools.py
endif

ifeq (true,$(call FEXISTS,factors.py))
FACTORS_PY:=../tools/factors.py
endif

ifeq (true,$(call FEXISTS,gradientmu.py))
GRADIENTMU_PY:=../tools/gradientmu.py
endif

.result.txt : answer.py $(MEMOIZE_PY) $(PRIMES_PY) $(GENTOOLS_PY) $(FACTORS_PY) $(GRADIENTMU_PY)
	./$< >$@
