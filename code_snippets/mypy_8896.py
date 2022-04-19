args = {'percent': percentage}
return cast(bool, await self._vehicle._command('set_charge_limit', args))
