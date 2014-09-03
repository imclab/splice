from splice.utils import environment_manager_create
from splice.environment import Environment

environment_manager_create()
env = Environment.instance()

from splice.queries import tile_stats_weekly, slot_stats_weekly, tile_stats_monthly, slot_stats_monthly

with env.application.app_context():
    conn = env.db.engine.connect()
    print "\ntile_stats_weekly - no tile_id"
    rval = tile_stats_weekly(conn, '2014-05-15')
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\ntile_stats_weekly - tile_id = 2"
    rval = tile_stats_weekly(conn, '2014-05-15', '2')
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\nslot_stats_weekly - no id"
    rval = slot_stats_weekly(conn, '2014-05-15')
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\nslot_stats_weekly - slot_id = 1"
    rval = slot_stats_weekly(conn, '2014-05-15', 1)
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\ntile_stats_monthly - no tile_id"
    rval = tile_stats_monthly(conn, '2014-05-15')
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\ntile_stats_monthly - tile_id = 2"
    rval = tile_stats_monthly(conn, '2014-05-15', '2')
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\nslot_stats_monthly - no id"
    rval = slot_stats_monthly(conn, '2014-05-15')
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

    print "\nslot_stats_monthly - slot_id = 1"
    rval = slot_stats_monthly(conn, '2014-05-15', 1)
    for week, tile_id, imps, clicks, pinned, blocked, spon, spon_link in rval:
        print week, tile_id, imps, clicks, pinned, blocked, spon, spon_link

