#pragma once
#include <gtk/gtk.h>

// typedef struct {
// 	GtkWidget* (*generate_widget)(void* menu_item);
// } MenuCallbacks;

typedef struct StickController StickController;
typedef void (*StickControllerCallback)(int dx, int dy, void* userdata);

/**
 * Installs CSS provider if it is not already installed.
 * This takes care of OSD colors and entire look-and-feel.
 */
void install_css_provider();
/**
 * (Re)installs CSS provider even if it was already installed.
 * Called after CSS color config is changed.
 */
void reconfigure_css_provider();

#define STICK_CONTROLLER_REPEAT_DELAY 200 /* ms */
/** Creates new StickController. Returns NULL on failure. */
StickController* stick_controller_create(StickControllerCallback cb, void* userdata);
/** Should be called from client's event callback */
void stick_controller_feed(StickController* sc, int values[]);
/** Frees StickController data */
void stick_controller_free(StickController* sc);
/** Converts KEY_* constant to GDK constant */
guint keycode_to_gdk_hw_keycode(int64_t key);

