TARGETS= pass1 fail1 pass2 fail2 pass3 fail3 pass4 fail4

# dodge for printing new lines
define NL


endef

header-targets:
	@echo available targets are:

list-targets:
	@$(foreach var,$(TARGETS), @echo $(var) $(NL) )

default: header-targets list-targets

clean:
	@del *.pass 2>null

targets: $(TARGETS)

pass1 pass2 pass3 pass4: pass%:
	@true

fail1 fail2 fail3 fail4: fail%:
	@$(if $(wildcard $@.pass) ,true, false)

fix1 fix2 fix3 fix4: fix%:
	@echo. > $@.pass

