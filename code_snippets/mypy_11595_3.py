if isinstance(forward_item, Instance):
    if forward_item.has_readable_member('__call__'):
        forward_item = self.expr_checker.analyze_external_member_access('__call__',
                                                                        forward_item,
                                                                        context)
