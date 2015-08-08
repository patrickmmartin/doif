TARGETS= pass1 pass2 fixable1 fixable2 broken1 broken2

action?=test

# defined to defer expansion until target execution 
define FIX_ACTION=
echo . > $@.pass
endef

define TEST_ACTION=
$(if $(wildcard $@.pass) ,true, false)
endef

define ECHO=
@echo running $@ $$action
endef


# dodge for printing new lines
define NL


endef

ifeq ($(OS),"Windows_NT")
  RM_SILENT=2>NUL del
else
  RM_SILENT=2>/dev/null rm
endif 

default: header-targets list-targets

header-targets:
	@echo available targets are:

list-targets:
	@$(foreach var,$(TARGETS), @echo $(var) $(NL) )

targets: $(TARGETS)

pass1 pass2 pass3 pass4: pass%:
	$(ECHO)
	@true

# targets broken after clean but can be fixed
fixable1 fixable2: fixable%:
	$(ECHO)
ifeq ($(action),fix)
	@$(FIX_ACTION)
else
	@$(TEST_ACTION)
endif

# targets that are always broken
broken1 broken2: broken%:
	$(ECHO)
	@false

# this will break fixable#n for you
clean:
	@-$(RM_SILENT) *.pass

# these will fix fixable#n for you
fix1 fix2: fix%:
	@echo .  > $(subst fix,fixable,$@.pass)

